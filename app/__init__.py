from flask import Flask, blueprints
from flask_cors import CORS
from app.api import api

app = Flask(__name__)
CORS(app)

app.register_blueprint(api)