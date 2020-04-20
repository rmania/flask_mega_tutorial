import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # value from ENV variable preferred, otherwise use hardcoded string
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    # if ENV not defined fallback var configuring a database named app.db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        "sqlite:///" + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
