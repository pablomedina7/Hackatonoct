from flask import Blueprint, jsonify, request
from services.happiness_services import calcular_felicidad

happiness_bp = Blueprint('felicidad', __name__)

@happiness_bp.route('/felicidad/<int:mascota_id>', methods=['GET'])
def obtener_felicidad(mascota_id):
    # Consultar la felicidad usando el servicio de felicidad
    estado_felicidad = calcular_felicidad(mascota_id)
    
    if estado_felicidad:
        return jsonify({"estado_felicidad": estado_felicidad}), 200
    else:
        return jsonify({"error": "No se pudo calcular la felicidad."}), 500
