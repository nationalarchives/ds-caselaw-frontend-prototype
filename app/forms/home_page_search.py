from flask_wtf import FlaskForm
from wtforms.fields import SearchField
from wtforms import BooleanField
from wtforms.validators import InputRequired

class HomePageSearch(FlaskForm):
    search_term = SearchField(
        'Search term',
        validators=[InputRequired()],
        render_kw={
            'class': 'search-component__search-term-input'
        }
    )
    neutral_citation = BooleanField('I\'m using a neutral citation, e.g. EWCA Civ 2781')
