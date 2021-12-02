from app import app
from flask import render_template, request
from content.recent_judgments import recent_judgments
from content.service_wide import service
from content.collections import collections
from content.search_results import search_results


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
    return render_template(
        'results.html',
        service=service,
        search_results=search_results
    )


@app.route('/browse')
def browse():
    return render_template(
        'browse.html',
        service=service,
    )


@app.route('/terms-of-use')
def terms_of_use():
    return render_template(
        'terms_of_use.html',
        service=service,
    )


@app.route('/open-justice-licence')
def open_justice_licence():
    return render_template(
        'open_justice_licence.html',
        service=service,
    )
