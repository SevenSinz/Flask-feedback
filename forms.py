from flask_wtf import FlaskForm
# from flask_wtf.html5 import URLField
from wtforms import StringField, FloatField, IntegerField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Email, Length
from wtforms.widgets import PasswordInput

class RegisterForm(FlaskForm):
    """ Form for Adding User to the user data table"""
    
    username = StringField(" Username: ",
                           validators=[InputRequired(), Length(min=1, max=20)])
    password = StringField(" Password: ",
                           validators=[InputRequired()],
                           widget=PasswordInput(hide_value=False))
    email = StringField(" Email: ",
                           validators=[InputRequired(), Email(), Length(min=1, max=50)])
    first_name = StringField(" First Name: ",
                           validators=[InputRequired(), Length(min=1, max=30)])
    last_name = StringField(" Last Name: ",
                           validators=[InputRequired(), Length(min=1, max=30)])
    
class LoginForm(FlaskForm):
    """ Form to login"""
    
    username = StringField(" Username: ",
                           validators=[InputRequired(), Length(min=1, max=20)])
    password = StringField(" Password: ",
                           validators=[InputRequired()],
                           widget=PasswordInput(hide_value=False))

class FeedbackForm(FlaskForm):    
    """ Form to Add and Update Feeback  """

    title = StringField(" Title: ",
                        validators=[InputRequired(), Length(min=1, max=100)])
    content = TextAreaField("Content: ",
                            validators=[InputRequired()])