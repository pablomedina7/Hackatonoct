from flask import Flask
from routes.adoption_routes import adopcion_bp
from models import db
from config import Config

# Crear la aplicación Flask
app = Flask(__name__)

# Aplicar la configuración
app.config.from_object(Config)

# Inicializar la base de datos
db.init_app(app)

# Registrar el blueprint de adopción
app.register_blueprint(adopcion_bp)

if __name__ == '__main__':
    # Crear las tablas de la base de datos si no existen
    with app.app_context():
        db.create_all()
    app.run(port=5001)