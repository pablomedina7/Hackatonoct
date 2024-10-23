from flask_sqlalchemy import SQLAlchemy
from datetime import datetime   
db = SQLAlchemy()
class mascota (db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    tipo = db.Column(db.String(120), nullable=False)
    raza = db.Column(db.String(120), nullable=False)
    sexo = db.Column(db.String(120), nullable=False)
    color = db.Column(db.String(120), nullable=False)
    fecha_adopcion = db.Column(db.Datetime, default=datetime.now, nullable=False)

# #documentación 
# Motivo: estamos creando el modelo Mascota que representa las mascotas adoptadas. Este modelo tiene 6 columnas importantes:
# id: Identificador único para la mascota.
# nombre: El nombre de la mascota.
# tipo: El tipo de la mascota.
#raza: La raza de la mascota.
# sexo: El sexo de la mascota (macho o hembra).
# fecha_adopcion: Fecha en que fue adoptada.