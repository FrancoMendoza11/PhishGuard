from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de entrada
class EmailInput(BaseModel):
    text: str

# Cargar modelo entrenado
model = joblib.load("model/phishing_model.pkl")

@app.post("/predict")
def predict_email(data: EmailInput):
    text = data.text
    prob = model.predict_proba([text])[0][1]
    label = "phishing" if prob > 0.5 else "legítimo"

    explanation = "El texto contiene términos asociados a fraude" if label == "phishing" else "El texto parece normal"

    return {
        "probability": float(prob),
        "label": label,
        "explanation": explanation
    }
