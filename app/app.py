from flask import Flask

# Local imports
from views import views_blueprint
from config import SECRET_KEY


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config["SECRET_KEY"] = SECRET_KEY

    if test_config:
        app.config.update(test_config)

    app.register_blueprint(views_blueprint)

    return app
