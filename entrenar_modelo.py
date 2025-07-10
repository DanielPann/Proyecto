import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
import os


X = np.array([
    [10, 90], [15, 85], [20, 80], [25, 75], [30, 70],
    [35, 65], [40, 60], [45, 55], [50, 50], [55, 45],
    [60, 40], [65, 35], [70, 30], [75, 25], [80, 20],
    [85, 15], [90, 10]
])


y = np.array([
    0.95, 0.90, 0.85, 0.80, 0.75,
    0.70, 0.65, 0.60, 0.55, 0.50,
    0.45, 0.40, 0.35, 0.30, 0.25,
    0.20, 0.15
])


modelo = LinearRegression()
modelo.fit(X, y)


os.makedirs("models", exist_ok=True)
with open("models/model.pkl", "wb") as f:
    pickle.dump(modelo, f)

print("✅ Modelo de regresión lineal entrenado y guardado como models/model.pkl")

