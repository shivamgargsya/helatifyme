# AnswerIQ Confidential and Proprietary

import logging
import time
import redis

from flask import request
from flask_caching import Cache
from flask_cors import CORS


from Config import config
import time


from flask_app_obj import get_flask_object



flask_app = get_flask_object()


cache = Cache(flask_app, config={'CACHE_TYPE': 'simple'})
#cache.clear()

# Setup Redis Cache
shared_cache = Cache(flask_app, config={
    'CACHE_TYPE': 'redis',
    'CACHE_KEY_PREFIX': 'SHARED',
    'CACHE_REDIS_HOST': config.redis_host(),
    'CACHE_REDIS_PORT': config.redis_port(),
    'CACHE_REDIS_PASSWORD': config.redis_password()
        })

# Clear Redis Cache on every application restart
shared_cache.clear()

CORS(flask_app, supports_credentials=True)



# Print immediately to stdout
log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)
logging.Formatter.converter = time.gmtime
logging.basicConfig(format='[%(asctime)s] %(levelname)s:%(message)s')


def get_flask_app():
    return flask_app


