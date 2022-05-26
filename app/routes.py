from app import app
from app.forms.home_page_search import HomePageSearch
from app.forms.structured_search_form import StructuredSearch
from app.helpers.applied_filters import remove_current_item_from_query_string, translate_to_human_readable_label, \
    filters_to_show
from flask import render_template, request, redirect, url_for, make_response
from content.service_wide import service
from content.search_results import search_results
from content.courts import courts
from content.sources import judgment_sources
from content.tribunals import tribunals


@app.route('/')
def home():
    form = HomePageSearch()

    return render_template(
        'home.html',
        service=service,
        tribunals=tribunals,
        courts=courts,
        form=form
    )


@app.route('/results', methods=['GET'])
def results():
    form = StructuredSearch(request.args)

    if form.search_term.data:

        # Dummy for a no results experience - search term is 'theory of everything'
        if form.search_term.data.lower() == 'theory of everything':
            return render_template(
                'no_results.html',
                service=service,
                form=form,
                remove_current_item_from_query_string=remove_current_item_from_query_string,
                translate_to_human_readable_label=translate_to_human_readable_label,
                filters_to_show=filters_to_show(request.args)
            )

    return render_template(
        'results.html',
        service=service,
        search_results=search_results,
        form=form,
        remove_current_item_from_query_string=remove_current_item_from_query_string,
        translate_to_human_readable_label=translate_to_human_readable_label,
        filters_to_show=filters_to_show(request.args)
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


@app.route('/judgment')
def judgment_quick_route():
    return redirect(url_for('judgment'))


@app.route('/judgment/formatted_from_print')
def judgment_quick_route_to_formatted_from_print():
    return redirect(url_for('judgment_formatted_from_print'))


@app.route('/ewhc/comm/2022/935')
def judgment():
    resp = make_response(render_template('judgment.html', service=service, print_format=False))
    return resp


@app.route('/ewhc/comm/2022/957/formatted_from_print')
def judgment_formatted_from_print():
    resp = make_response(render_template('judgment_formatted_from_print.html', service=service, print_format=True))
    return resp


@app.route('/search')
def structured_search():
    form = StructuredSearch()

    return render_template(
        'structured_search.html',
        service=service,
        form=form
    )


@app.route('/sources')
def sources():
    return render_template(
        'sources.html',
        service=service,
        sources=judgment_sources
    )


@app.route('/what_to_expect')
def what_to_expect():
    return render_template(
        'what_to_expact.html',
        service=service
    )


@app.route('/accessibility-statement')
def accessibility_statement():
    return render_template(
        'accessibility_statement.html',
        service=service
    )

@app.route('/transactional-licence-form')
def transactional_licence_form():
    return render_template(
        'transactional_licence_form.html',
        service=service,
    )

