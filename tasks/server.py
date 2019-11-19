# Wise.io and GE Confidential and Proprietary

from flask_failsafe import failsafe
from fabric.api import task, local


@failsafe
def server_app():
    from flask_app import flask_app
    return flask_app


@task()
def flask(host="0.0.0.0", port=8080):
    """Runs a development server."""
    server_app().run(host=host, port=port)


@task(default="true")
def server(port=5000):
    local("echo \"fab server.flask\\nfab jobs\""
          # xargs is a quick hack for local concurrency:
          "| xargs -I CMD -P3 bash -c CMD")


# Added for debugging purpose on PyCharm
if __name__ == "__main__":
    flask()