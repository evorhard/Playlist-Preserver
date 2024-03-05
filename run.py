import sys

sys.path.append("app")

from app import create_app, create_celery

app = create_app()
celery = create_celery(app)

if __name__ == "__main__":
    app.run(debug=True)
