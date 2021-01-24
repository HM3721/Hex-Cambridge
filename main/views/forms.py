from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

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
    
    #recaptcha = RecaptchaField()
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        [DataRequired()]
    )

    password = StringField(
        'Password',
        [DataRequired()]
    )
    remember = BooleanField('remember me')

    submit = SubmitField('Submit')

class SignupForm(FlaskForm):

    fname = StringField('First Name', [
        DataRequired(message='PLease enter your first name'),
        DataRequired()])
    lname = StringField('Last Name', [
        DataRequired(message='PLease enter your last name'),
        DataRequired()])    
    email = StringField('Email address', [
        Email(message='Not a valid email address.'),
        DataRequired()])
    password = PasswordField('Password', [
        DataRequired(message="Please enter a password."),
        Length(min=6, message='Select a stronger password.')
    ])

    remember_me = BooleanField('Remember Me', default=False)
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


    
