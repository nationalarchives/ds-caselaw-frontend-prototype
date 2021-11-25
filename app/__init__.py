from flask import Flask

app = Flask(__name__, static_url_path="/frontendproto/static", static_folder="static")

from app import routes