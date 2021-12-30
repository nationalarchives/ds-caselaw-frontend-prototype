import datetime
from flask_wtf import FlaskForm
from wtforms.fields import SearchField
from wtforms import BooleanField, StringField, SelectField, DateField
from wtforms.validators import InputRequired
from content.courts import courts

formatted_courts = [('all', 'All courts')] + [(court['code'], court['name']) for court in courts]
formatted_collections = [('all', 'All collections')] + [(court['code'], court['code']) for court in courts]
now = datetime.datetime.now()


class StructuredSearch(FlaskForm):
    search_term = SearchField(
        'Search term',
        render_kw={'class': 'search-component__search-term-input'},
        validators=[InputRequired()]
    )
    neutral_citation = BooleanField('I\'m using a neutral citation, e.g. EWCA Civ 2781')
    party_name = StringField(
        'Party name',
        description='For example a claimant, defendant or prosecutor',
        render_kw={
            'class': 'structured-search__name-input'
        })
    judge_name = StringField(
        'Judge name',
        description="For example 'Smith', 'Judge Smith' or 'Lord Justice Smith'",
        render_kw={
            'class': 'structured-search__name-input'
        })
    courts = SelectField(
        'From a specific court',
        choices=formatted_courts,
        render_kw={
            'class': 'structured-search__select'
        }
    )
    collections = SelectField(
        'From a specific collection',
        choices=formatted_collections,
        render_kw={
            'class': 'structured-search__select'
        }
    )
    from_date = DateField(
        'From date',
        render_kw={
            'class': 'structured-search__date-input',
            'min': '2003-01-02',
            'max': f"{now.year}-{now.month}-{now.day}",
            'placeholder': 'YYYY-MM-DD'
        }
    )
    to_date = DateField(
        'To date',
        render_kw={
            'class': 'structured-search__date-input',
            'min': '2003-01-02',
            'max': f"{now.year}-{now.month}-{now.day}",
            'placeholder': 'YYYY-MM-DD'
        }
    )
