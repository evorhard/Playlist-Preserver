from celery import Celery
from flask import Flask

# Local imports
from views import views_blueprint
from config import SECRET_KEY


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["CELERY_BROKER_URL"] = "redis://localhost:6379/0"
    app.config["CELERY_RESULT_BACKEND"] = "redis://localhost:6379/0"

    if test_config:
        app.config.update(test_config)

    app.register_blueprint(views_blueprint)

    return app


def create_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config["CELERY_RESULT_BACKEND"],
        broker=app.config["CELERY_BROKER_URL"],
    )
    celery.conf.update(app.config)

    return celery
