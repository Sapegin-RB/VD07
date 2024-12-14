from flask import Flask
from flask_wtf import CSRFProtect

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    csrf.init_app(app)

    # Регистрация маршрутов
    from .routes import bp
    app.register_blueprint(bp)

    return app
