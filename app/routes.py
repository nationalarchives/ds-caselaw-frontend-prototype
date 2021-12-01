from app import app
from flask import render_template, request
from content.recent_judgments import recent_judgments
from content.service_wide import service
from content.collections import collections


@app.route('/')
def home():
    return render_template(
        'home.html',
        service=service,
        recent_judgments=recent_judgments,
        collections=collections
    )


@app.route('/search', methods=['GET'])
def search():
    return request.args['collection']


@app.route('/terms-of-use')
def terms_of_use():
    return render_template('terms-of-use.html')

@app.route('/browse')
def browse():
    return render_template('browse.html')
