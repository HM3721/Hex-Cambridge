"""Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length

class ListingForm(FlaskForm):
    """Listing Form."""

    name = StringField(
        'Student Name',
        [DataRequired()]
    )

    institution = StringField(
        'Institution',
        [DataRequired()])

    category_of_resource = StringField(
        'Category of Resource',
        [DataRequired()])

    name_of_resource = StringField(
        'Name of Resource',
        [DataRequired()])

    further_description = StringField(
        'Further Description',
        [DataRequired()]
        )
    
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')


    
