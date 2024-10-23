from flask import Blueprint, request, jsonify
from models import db, mascota
from datetime import datetime

adopcion_bp = Blueprint('adopcion', __name__)

@adopcion_bp.route('/adoptar', methods=['POST'])
def adoptar_mascota():
    # Obtener datos enviados en el cuerpo del POST request
    data = request.json

    nombre = data.get('nombre')
    tipo = data.get('tipo')
    raza = data.get('raza')
    sexo = data.get('sexo')
    color = data.get('color')

    # Verificamos si faltan datos requeridos
    if not nombre or not tipo or not raza or not sexo or not color:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Creamos una nueva instancia del modelo 'mascota' con los datos proporcionados
    nueva_mascota = mascota(
        nombre=nombre,
        tipo=tipo,
        raza=raza,
        sexo=sexo,
        color=color,
        fecha_adopcion=datetime.now()
    )
    try:
        db.session.add(nueva_mascota)
        db.session.commit()
        return jsonify({"mensaje": f"La mascota {nombre} ha sido adoptada con éxito."}), 201
    except Exception as e:
        db.session.rollback()  # Si hay algún error, revertimos la operación
        return jsonify({"error": f"Error al adoptar la mascota: {str(e)}"}), 500
