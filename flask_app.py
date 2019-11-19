# AnswerIQ Confidential and Proprietary

import logging
import time
import redis

from flask import request
from flask_caching import Cache
from flask_cors import CORS

from dotenv import load_dotenv
import os
from pathlib import Path  # python3 only
dir_path=os.path.dirname(os.path.abspath(__file__))
env_path = dir_path+  '/.env'
load_dotenv(dotenv_path=env_path)


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

from hora.notification.queue.Fifo_queue import Fifo_queue
from hora.notification.queue.Queue_registry import Queue_registry
from hora.notification.dispatcher.dispatcher import Dispatcher

def setup():
    queue=Fifo_queue('consumer_action_queue')
    Queue_registry.getInstance().register('consumer_action_queue',queue)

def dispatcher_job():
    while True:
        try:
            queues=Queue_registry.getInstance().get_queues()
            for queue in queues:
                Dispatcher(list(queue.values())[0]).dispatch_items()
                time.sleep(10)
        except Exception as e:
            print(str(e))



from hora.consumer.resources.consumer_resources import *
from hora.worker.resources.worker_resource import *
from hora.tasks.resources.task_resource import *
from hora.category.resources.category_resource import *
from hora.commons.resources.authorisation.authorisation_resource import *
from hora.commons.resources.health_check import *
from hora.ratings.resources.ratings_resource import *


setup()

from time import sleep
from concurrent.futures import ThreadPoolExecutor

# DOCS https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
executor = ThreadPoolExecutor(1)
poll_executor=ThreadPoolExecutor(1)
poll_executor.submit(dispatcher_job)

