from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///predicciones.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Prediccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ciclistas = db.Column(db.Float, nullable=False)
    fumadores = db.Column(db.Float, nullable=False)
    resultado = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)


modelo = pickle.load(open('models/model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    ciclistas = float(request.form['ciclistas'])
    fumadores = float(request.form['fumadores'])
    entrada = np.array([[ciclistas, fumadores]])
    
    probabilidad = modelo.predict(entrada)[0]
    porcentaje = round(probabilidad * 100, 2)

    nueva = Prediccion(ciclistas=ciclistas, fumadores=fumadores, resultado=porcentaje)
    db.session.add(nueva)
    db.session.commit()

    return render_template('index.html', prediction_text=f"Riesgo estimado: {porcentaje:.2f}%")


@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.get_json()
    ciclistas = float(data['ciclistas'])
    fumadores = float(data['fumadores'])
    entrada = np.array([[ciclistas, fumadores]])
    
    probabilidad = modelo.predict(entrada)[0]
    porcentaje = round(probabilidad * 100, 2)

    nueva = Prediccion(ciclistas=ciclistas, fumadores=fumadores, resultado=porcentaje)
    db.session.add(nueva)
    db.session.commit()

    return jsonify({'riesgo_estimado': porcentaje})


@app.route('/historial')
def historial():
    registros = Prediccion.query.order_by(Prediccion.fecha.desc()).limit(10).all()
    registros = registros[::-1]  
    return render_template('historial.html', registros=registros)


if __name__ == '__main__':
    os.makedirs('db', exist_ok=True)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
