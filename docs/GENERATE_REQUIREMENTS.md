# Generate requirements after final testing

Run in a Colab cell from the project root:

```python
from importlib.metadata import version, PackageNotFoundError
packages = ['pandas','numpy','scikit-learn','xgboost','lightgbm','catboost','shap','lime','matplotlib','seaborn','plotly','joblib','fastapi','uvicorn','pydantic','httpx']
lines = []
for package in packages:
    try: lines.append(f'{package}=={version(package)}')
    except PackageNotFoundError: print('Not installed:', package)
open('requirements.txt','w').write('\n'.join(lines)+'\n')
```

Check that the installed versions reproduce the trained model and API before publishing.
