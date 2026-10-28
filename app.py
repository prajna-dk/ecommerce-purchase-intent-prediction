"""Optional prediction API: uvicorn app:app --reload (from project root)."""
import json
from pathlib import Path
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from helpers import predict_one

app = FastAPI(title='Purchase Intent API')
ROOT = Path(__file__).resolve().parent
model = joblib.load(ROOT / 'models/final_model.joblib')
threshold = float(json.loads((ROOT / 'models/model_info.json').read_text())['threshold'])

class Session(BaseModel):
    Administrative: int = 0
    Administrative_Duration: float = 0.0
    Informational: int = 0
    Informational_Duration: float = 0.0
    ProductRelated: int = 0
    ProductRelated_Duration: float = 0.0
    BounceRates: float = 0.0
    ExitRates: float = 0.0
    PageValues: float = 0.0
    SpecialDay: float = 0.0
    Month: str
    OperatingSystems: int
    Browser: int
    Region: int
    TrafficType: int
    VisitorType: str
    Weekend: bool = False

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.post('/predict')
def predict(session: Session):
    return predict_one(session.model_dump(), model, threshold)
