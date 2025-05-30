import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# 1. Carga .env
load_dotenv()

app = Flask(__name__)

# 2. Configura la base de datos usando DATABASE_URL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Ejemplo de modelo: ficha de estudiante
class Ficha(db.Model):
    __tablename__ = 'fichas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    curso = db.Column(db.String(50), nullable=False)
    diagnostico = db.Column(db.String(200), nullable=True)

@app.route('/fichas', methods=['GET'])
def listar_fichas():
    todas = Ficha.query.all()
    return jsonify([{'id': f.id, 'nombre': f.nombre, 'curso': f.curso, 'diagnostico': f.diagnostico} for f in todas])

@app.route('/fichas', methods=['POST'])
def crear_ficha():
    data = request.json
    f = Ficha(nombre=data['nombre'], curso=data['curso'], diagnostico=data.get('diagnostico'))
    db.session.add(f)
    db.session.commit()
    return jsonify({'id': f.id}), 201

if __name__ == '__main__':
    # Crea las tablas al iniciar (solo en desarrollo)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8000)
