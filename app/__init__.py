from flask import Flask
from config import Config
from .animais import animais
from .paises import paises

def create_app():
    app = Flask('__main__')
    app.config.from_object(Config)
    app.register_blueprint(animais, url_prefix='/animais')
    app.register_blueprint(paises, url_prefix='/paises')
        
    return app  