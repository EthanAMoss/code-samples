from flask_wtf import FlaskForm as Form
from wtforms import StringField, DecimalField, DateField, RadioField, SelectField, BooleanField, SelectMultipleField
from wtforms.validators import DataRequired


class TestForm(Form):
    date_field = DateField('Your Birthdate (MM/DD/YYYY): ', format='%d/%m/%Y')
    select_field = SelectField('Your Gender',
                               choices=[('Male', 'Male'), ('Female', 'Female'),
                                        ('Other', 'Other')], default='Other')
    bool_field = BooleanField('Check this box if you are a human:', default=False)
    radio_field = RadioField('Cola Preference',
                             choices=[('Coke', 'Coca-Cola'), ('Pepsi', 'Pepsi'),
                                      ('Oh God Why', 'RC Cola')],
                             default=None)
    dec_field = DecimalField('What do you think your current GPA is?')
    str_field = StringField('Put A Name in Here (Doesn\'t Have to be yours)')
