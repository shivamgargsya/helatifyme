# AnswerIQ Confidential and Proprietary
from flask_app_obj import flask_app
from flask import Blueprint
from flask_restplus import Api

apiv1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(apiv1, version='1.0', title='RPA v1 APIs', description='v1 apis')


healthcheck_api = api.namespace('Health Check APIs', description='Health Check API methods', path='/')


recepie_api=api.namespace('Recepie',description='API for Recepie adding operations ',path='/')
flask_app.register_blueprint(apiv1)