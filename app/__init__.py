from flask import Flask
from flask_compress import Compress
import os
SECRET_KEY = os.urandom(32)[0:5]

app = Flask(__name__, static_url_path="/static", static_folder="static")
app.config['SECRET_KEY'] = SECRET_KEY

Compress(app)
from app import routes
