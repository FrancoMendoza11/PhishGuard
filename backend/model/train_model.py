import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import joblib

# 1. Dataset de ejemplo
data = {
    "text": [
        "Actualiza tu cuenta bancaria ahora haciendo clic aquí",
        "Tu factura de luz está lista para descargar",
        "Ganaste un iPhone, ingresa tus datos para recibirlo",
        "Recordatorio: reunión del equipo mañana a las 10am",
        "Confirma tu contraseña para evitar suspensión de cuenta",
        "Tu pedido fue enviado, gracias por tu compra"
    ],
    "label": [1, 0, 1, 0, 1, 0]  # 1 = phishing, 0 = legítimo
}

df = pd.DataFrame(data)

# 2. Dividir los datos
X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["label"], test_size=0.2, random_state=42
)

# 3. Crear el pipeline (vectorizador + clasificador)
model = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words=None)),
    ("clf", LogisticRegression())
])

# 4. Entrenar el modelo
model.fit(X_train, y_train)

# 5. Evaluar el modelo
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {acc * 100:.2f}%")

# 6. Guardar el modelo
joblib.dump(model, "phishing_model.pkl")
print("✅ Modelo guardado como phishing_model.pkl")
