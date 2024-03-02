import os

from dotenv import load_dotenv

load_dotenv()

# .env globals
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = "http://localhost:5000/callback"
AUTHORIZATION_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
CELERY_BROKER_URL = "redis://localhost:5000/0"
CELERY_RESULT_BACKEND = "redis://localhost:5000/0"

# Other globals
SCOPE = "user-read-private user-read-email"
