"""Shared, simple preprocessing and scoring utilities."""
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, OneHotEncoder, RobustScaler

TARGET = 'Converted'
NUMBER_COLS = ['Administrative', 'Informational', 'ProductRelated', 'BounceRates', 'ExitRates', 'SpecialDay']
SKEWED_COLS = ['Administrative_Duration', 'Informational_Duration', 'ProductRelated_Duration', 'PageValues']
CATEGORY_COLS = ['Month', 'OperatingSystems', 'Browser', 'Region', 'TrafficType', 'VisitorType']
NEW_NUMBER_COLS = ['total_pages', 'product_page_share', 'product_time_share']
NEW_SKEWED_COLS = ['total_duration', 'avg_time_per_page']

# Illustrative assumptions only; confirm with stakeholders before Stage 6.
CONVERSION_VALUE = 50
NUDGE_COST = 5
NUDGE_SUCCESS = 0.2

def add_features(df):
    """Derive page totals, time totals, shares and a returning-visitor flag."""
    out = df.copy()
    pages = out['Administrative'] + out['Informational'] + out['ProductRelated']
    seconds = out['Administrative_Duration'] + out['Informational_Duration'] + out['ProductRelated_Duration']
    out['total_pages'] = pages
    out['total_duration'] = seconds
    out['avg_time_per_page'] = (seconds / pages.replace(0, np.nan)).fillna(0)
    out['product_page_share'] = (out['ProductRelated'] / pages.replace(0, np.nan)).fillna(0)
    out['product_time_share'] = (out['ProductRelated_Duration'] / seconds.replace(0, np.nan)).fillna(0)
    out['is_returning'] = (out['VisitorType'] == 'Returning_Visitor').astype(int)
    return out

def build_pipeline(model, use_pagevalues=True):
    """Feature engineering, transformations, and estimator fitted together."""
    skewed = SKEWED_COLS + NEW_SKEWED_COLS
    if not use_pagevalues:
        skewed = [c for c in skewed if c != 'PageValues']
    log_then_scale = Pipeline([
        ('log', FunctionTransformer(np.log1p, feature_names_out='one-to-one')),
        ('scale', RobustScaler()),
    ])
    prepare = ColumnTransformer([
        ('numbers', RobustScaler(), NUMBER_COLS + NEW_NUMBER_COLS),
        ('skewed', log_then_scale, skewed),
        ('categories', OneHotEncoder(handle_unknown='ignore', sparse_output=False), CATEGORY_COLS),
        ('flags', 'passthrough', ['Weekend', 'is_returning']),
    ])
    return Pipeline([('features', FunctionTransformer(add_features)), ('prep', prepare), ('model', model)])

def load_train_test():
    """Return model inputs and labels without session IDs."""
    train, test = pd.read_csv('data/train.csv'), pd.read_csv('data/test.csv')
    drop = [TARGET, 'session_id']
    return train.drop(columns=drop), train[TARGET], test.drop(columns=drop), test[TARGET]

def threshold_table(y_true, proba):
    """Calculate flagging volume, precision, recall and illustrative net value."""
    y_true, proba = np.asarray(y_true), np.asarray(proba)
    rows = []
    for t in np.arange(0.05, 0.96, 0.01):
        flagged = proba >= t
        n_flagged = int(flagged.sum())
        caught = int((flagged & (y_true == 1)).sum())
        buyers = int((y_true == 1).sum())
        rows.append({'threshold': round(float(t), 2),
                     'sessions_flagged': n_flagged, 'true_buyers_caught': caught,
                     'prec': round(caught / n_flagged, 4) if n_flagged else 0.0,
                     'rec': round(caught / buyers, 4) if buyers else 0.0,
                     'net_value': round(caught * CONVERSION_VALUE * NUDGE_SUCCESS - n_flagged * NUDGE_COST, 2)})
    return pd.DataFrame(rows)

def original_name(encoded_name):
    """Map transformed feature names back to their source columns."""
    kind, _, rest = encoded_name.partition('__')
    if kind == 'categories':
        for col in CATEGORY_COLS:
            if rest.startswith(col + '_'):
                return col
    return rest

def top_drivers(shap_table, k=3):
    """Find the strongest absolute attribution values per session."""
    rows = []
    for _, row in shap_table.iterrows():
        top = row.reindex(row.abs().sort_values(ascending=False).index)[:k]
        labels = [str(name) + (' (+)' if value > 0 else ' (-)') for name, value in top.items()]
        rows.append(labels + [None] * (k - len(labels)))
    return pd.DataFrame(rows, columns=['top_driver_' + str(i + 1) for i in range(k)])

def predict_one(session, model, threshold):
    """Score one session using the fitted pipeline."""
    row = pd.DataFrame([session])
    row['Weekend'] = row['Weekend'].astype(int)
    proba = float(model.predict_proba(row)[0, 1])
    return {'probability': round(proba, 4), 'will_convert': bool(proba >= threshold)}
