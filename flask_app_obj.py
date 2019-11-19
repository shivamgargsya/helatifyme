import itsdangerous
from flask import Flask
from flask_failsafe import failsafe

from Config import config

flask_app_obj = None

@failsafe
def get_flask_object():
    global flask_app_obj
    if flask_app_obj is None:
        flask_app_obj = Flask(__name__)
        flask_app_obj.debug = config.debug()
        flask_app_obj.config.update(
            SESSION_COOKIE_HTTPONLY=(config.env() != 'dev'),
            SESSION_COOKIE_SECURE=(config.env() != 'dev'),
            #SQLALCHEMY_DATABASE_URI=config.database_connection_string(),
            #SQLALCHEMY_POOL_RECYCLE=150
        )

        flask_app_obj.secret_key = config.secret_key()
        flask_app_obj.signer = itsdangerous.URLSafeTimedSerializer(flask_app_obj.secret_key)

        flask_app_obj.config['CORS_HEADERS'] = "Content-Type", "Authorization"
        flask_app_obj.config['CORS_RESOURCES'] = {
            r"/api/*": {
                "origins": config.allowed_origins()
            }
        }

    return flask_app_obj


flask_app = get_flask_object()
