import os
import dotenv


dotenv.load_dotenv()


class Config(object):
    CSRF_ENABLED = True
    DATABASE_URL = os.environ["DATABASE_URL"]
    SECRET_KEY = os.environ["DATABASE_SECRET"]


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    