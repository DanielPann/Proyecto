Predicción de Enfermedades Cardíacas con Flask y Machine Learning

Este es el proyecto final para el curso de Programación Avanzada. La aplicación web permite predecir el riesgo de enfermedades cardíacas en función del porcentaje de personas que montan bicicleta y el porcentaje de fumadores. Utiliza Flask, regresión lineal, SQLAlchemy, y una API RESTful.

Tecnologías utilizadas:
- Python 3.11
- Flask
- SQLAlchemy + SQLite
- Scikit-learn
- Bootstrap 5
- Chart.js
- Postman (para pruebas de API)

Características principales:
- Predicción de riesgo con regresión lineal (0–100%)
- Almacenamiento de predicciones en base de datos
- Interfaz web simple y responsiva
- Historial con gráfica de resultados (Chart.js)
- API RESTful que acepta y responde en JSON

Ejecución del proyecto:

1. Clona el repositorio
git clone https://github.com/TU_USUARIO/proyecto-final-flask.git
cd proyecto-final-flask

2. Crea un entorno virtual e instala dependencias
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Entrena el modelo (una sola vez)
python entrenar_modelo.py

4. Ejecuta la aplicación Flask
python app.py

5. Abre en el navegador:
Formulario: http://127.0.0.1:5000
Historial: http://127.0.0.1:5000/historial

6. Prueba la API con Postman:
Endpoint: POST http://127.0.0.1:5000/api/predict
Body (JSON):
{
  "ciclistas": 30,
  "fumadores": 60
}

Respuesta esperada:
{
  "riesgo_estimado": 72.5
}

📄 Archivos importantes
- app.py – Aplicación principal Flask
- entrenar_modelo.py – Script para entrenar y guardar el modelo
- models/model.pkl – Modelo entrenado
- templates/index.html – Formulario web
- templates/historial.html – Tabla + gráfica de historial
- requirements.txt – Dependencias



Autor:
Daniel Gómez – Proyecto Final – Programación Avanzada
