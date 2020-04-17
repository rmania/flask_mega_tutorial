import os

class Config(object):
    # value from ENV variable preferred, otherwise use hardcoded string
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
