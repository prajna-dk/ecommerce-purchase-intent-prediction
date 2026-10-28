"""Recreate evaluation outputs from existing scores without fitting a model.
Run from project root: python scripts/evaluate_saved_scores.py
Requires pandas, numpy, matplotlib, scikit-learn.
"""
from pathlib import Path
import pandas as pd,numpy as np,json,matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.metrics import average_precision_score,roc_auc_score,brier_score_loss,log_loss
root=Path(__file__).resolve().parents[1];reports=root/"reports";reports.mkdir(exist_ok=True)
s=pd.read_csv(root/'bi/sessions_scored.csv');tr=pd.read_csv(root/'data/train.csv');te=pd.read_csv(root/'data/test.csv');meta=json.loads((root/'models/model_info.json').read_text())
def join(df,source):
 j=df[['session_id','Converted']].merge(s[['session_id','probability','score_source','predicted']],on='session_id',validate='one_to_one');assert (j.score_source==source).all();assert len(j)==len(df);return j
train=join(tr,'train_oof');test=join(te,'test_holdout');
def metrics(df):
 y=df.Converted.to_numpy();p=df.probability.to_numpy(); base=y.mean();return {'rows':len(df),'buyers':int(y.sum()),'prevalence':base,'model_pr_auc':average_precision_score(y,p),'random_rank_expected_pr_auc':base,'model_roc_auc':roc_auc_score(y,p),'brier_model':brier_score_loss(y,p),'brier_constant_prevalence':brier_score_loss(y,np.full(len(y),base)),'log_loss_model':log_loss(y,np.clip(p,1e-12,1-1e-12)),'log_loss_constant_prevalence':log_loss(y,np.full(len(y),base))}
a=metrics(train);b=metrics(test)
# reliability bins equal-frequency; no fitted calibration / leakage
bins=[]
for label,df in [('train_oof',train),('test_holdout',test)]:
 x=df.copy();x['bin']=pd.qcut(x.probability,10,labels=False,duplicates='drop');g=x.groupby('bin',observed=True).agg(n=('Converted','size'),mean_predicted=('probability','mean'),observed_conversion=('Converted','mean'),buyers=('Converted','sum')).reset_index();g.insert(0,'split',label);bins.append(g)
bins=pd.concat(bins,ignore_index=True);bins.to_csv(reports/'calibration_reliability_bins.csv',index=False)
plt.figure(figsize=(7,5));plt.plot([0,1],[0,1],'--',label='Perfect calibration')
for name,group in bins.groupby('split'):plt.plot(group.mean_predicted,group.observed_conversion,'o-',label=name)
plt.xlabel('Mean predicted score');plt.ylabel('Observed purchase rate');plt.title('Reliability diagram (10 quantile bins)');plt.legend();plt.grid(alpha=.2);plt.tight_layout();plt.savefig(reports/'calibration_reliability.png',dpi=160);plt.close()
# sensitivity on OOF training only, using existing threshold table and saved assumptions
th=pd.read_csv(root/'bi/threshold_table.csv');cv=meta['conversion_value'];ns=meta['nudge_success'];cost=meta['nudge_cost'];
scenarios=[('base',cv,ns,cost),('lower_effect',cv,ns/2,cost),('higher_effect',cv,ns*1.5,cost),('higher_cost',cv,ns,cost*1.5),('lower_cost',cv,ns,cost/2)]
rows=[]
for label,value,effect,c in scenarios:
 d=th.copy();d['estimated_net_value']=d.true_buyers_caught*value*effect-d.sessions_flagged*c;best=d.sort_values(['estimated_net_value','threshold'],ascending=[False,True]).iloc[0];sel=d.iloc[(d.threshold-meta['threshold']).abs().argmin()]
 rows.append({'scenario':label,'conversion_value':value,'assumed_success_rate':effect,'cost_per_flag':c,'optimal_threshold_on_training_oof':best.threshold,'max_estimated_net_value_training_oof':best.estimated_net_value,'net_value_at_selected_threshold_training_oof':sel.estimated_net_value})
sensitivity=pd.DataFrame(rows);sensitivity.to_csv(reports/'business_impact_sensitivity.csv',index=False)
# test illustrative evaluation at fixed preselected threshold, no tuning
TP=int(((test.Converted==1)&(test.predicted==1)).sum());FP=int(((test.Converted==0)&(test.predicted==1)).sum());FN=int(((test.Converted==1)&(test.predicted==0)).sum());TN=int(((test.Converted==0)&(test.predicted==0)).sum());test_net=TP*cv*ns-(TP+FP)*cost
summary={'train_oof':a,'test_holdout':b,'selected_threshold':meta['threshold'],'test_confusion_matrix':{'TN':TN,'FP':FP,'FN':FN,'TP':TP},'test_illustrative_net_value':test_net,'assumptions':{'conversion_value':cv,'nudge_success':ns,'nudge_cost':cost}}
(reports/'evaluation_addendum_metrics.json').write_text(json.dumps(summary,indent=2))

print("Evaluation metrics, calibration chart, and sensitivity table regenerated in reports/")
