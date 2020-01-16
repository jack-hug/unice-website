from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email,Regexp,EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    password = PasswordField('密码',validators=[DataRequired()])
    submit = SubmitField('登录')
