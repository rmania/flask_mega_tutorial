from flask import Flask

app = Flask(__name__)

# workaround to circular imports
from app import routes