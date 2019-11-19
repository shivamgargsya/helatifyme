import json
from functools import wraps
from flask import request

def handle_exception(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            if "client_id" in kwargs:
                e.message = "Error occured while checking client-id {0}, ".format(kwargs['client_id']) + e.message
            print(str(e))
            return "Internal server error", 500

    return wrapper


def check_json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not request.headers['Content-Type'] == 'application/json':
            msg = "Application expects json body"
            return dict(status=415, message=msg), 415
        try:
            json.loads(request.data)
        except Exception:
            msg = 'Failed to convert request data into a json object'
            return dict(status=415, message=msg), 415
        return f(*args, **kwargs)

    return wrapper