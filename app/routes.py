from app import app
import re
from flask import render_template, request, redirect, url_for, make_response
from content.recent_judgments import recent_judgments
from content.service_wide import service
from content.search_results import search_results
from content.courts import courts


@app.route('/')
def home():
    return render_template(
        'home.html',
        service=service,
        recent_judgments=recent_judgments,
        courts=courts
    )


@app.route('/search', methods=['GET'])
def search():
    return render_template(
        'results.html',
        service=service,
        courts=courts,
        search_results=search_results
    )

@app.route('/terms-of-use')
def terms_of_use():
    return render_template(
        'terms_of_use.html',
        service=service,
    )


@app.route('/neutral-citation/')
def neutral_citation():
    neutral_citation = request.args['neutral_citation']

    if re.match(r'^\[\d{4}\]\s?\w{3,4}\s?\w{3}\s?\d{4}$', neutral_citation):
        return render_template(
            'judgment.html',
            service=service
        )

    if re.match(r'(?=.*\[\d{4}\])(?=.*\w).{8,25}', neutral_citation):
        return redirect(url_for('disambiguation', neutral_citation=neutral_citation))

    return redirect(url_for('no_results', search_term=neutral_citation))


@app.route('/disambiguation/')
def disambiguation():
    return render_template(
        'disambiguation.html',
        service=service,
        neutral_citation=request.args['neutral_citation']
    )


@app.route('/no-results/')
def no_results():
    return render_template(
        'no_results.html',
        service=service,
        search_term=request.args['search_term']
    )


@app.route('/open-justice-licence')
def open_justice_licence():
    return render_template(
        'open_justice_licence.html',
        service=service,
    )

@app.route('/judgment')
def judgment_quick_route():
    return redirect(url_for('judgment'))

@app.route('/ewhc/admin/2021/3290')
def judgment():
    resp = make_response(render_template('judgment.html'))
    resp.headers['Content-Security-Policy'] = "script-src 'nonce-2wCEAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRo' " \
                                              "'strict-dynamic' " \
                                              "'unsafe-inline' " \
                                              "https:;" \
                                              "object-src 'none';" \
                                              "base-uri 'none';"
    return resp

@app.route('/structured-search')
def structured_search():
    return render_template(
        'structured_search.html',
        service=service
    )