import os
import dotenv


dotenv.load_dotenv()


class Config(object):
    CSRF_ENABLED = True


class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URL = os.environ['PRODUCTION_DATABASE_URL']
    SECRET_KEY = os.environ['PRODUCTION_DATABASE_SECRET']


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URL = os.environ['DEVELOPMENT_DATABASE_URL']
    SECRET_KEY = os.environ['DEVELOPMENT_DATABASE_SECRET']
    