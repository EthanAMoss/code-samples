from flask_wtf import FlaskForm as Form
from wtforms import StringField, DecimalField
from wtforms.validators import DataRequired


class SearchForm(Form):
    search_text = StringField(u'I want to find...', validators=[DataRequired()])
    search_radius = DecimalField(u'Within', places=1, validators=[DataRequired()], default=3.0)
