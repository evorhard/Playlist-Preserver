from flask import Flask

# Local imports
from config import APP_SECRET
from views import views_blueprint


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.secret_key = APP_SECRET

    if test_config:
        app.config.update(test_config)

    app.register_blueprint(views_blueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", debug=True)
