import os
from datetime import timedelta


JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
DATABASE_URL = os.getenv("DB_URL")
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)