# AnswerIQ Confidential and Proprietary
from flask_app_obj import flask_app
from flask import Blueprint
from flask_restplus import Api

apiv1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(apiv1, version='1.0', title='RPA v1 APIs', description='v1 apis')


healthcheck_api = api.namespace('Health Check APIs', description='Health Check API methods', path='/')

auth_api=api.namespace('Authorisation',description='',path='/')
task_api=api.namespace('Task',description='API for CRU operations and get tasks related to worker consumer ',path='/')
worker_api=api.namespace('Worker',description='API for CRU operations on workers ',path='/')
consumer_api=api.namespace('Consumer',description='API for CRU operations on consumers ',path='/')
category_api=api.namespace('Category',description='API for CRU operations on categories ',path='/')
rating_api=api.namespace('Rating',description='API for CRU operations on ratings ',path='/')
flask_app.register_blueprint(apiv1)