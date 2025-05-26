from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, FloatField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    full_name = StringField('Full Name', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EnrollmentForm(FlaskForm):
    roll_number = StringField('Roll Number', validators=[DataRequired()])
    department = SelectField('Department', choices=[
        ('cse', 'Computer Science'),
        ('ece', 'Electronics'),
        ('mech', 'Mechanical'),
        ('civil', 'Civil'),
        ('it', 'Information Technology')
    ], validators=[DataRequired()])
    cgpa = FloatField('CGPA', validators=[DataRequired()])
    graduation_year = SelectField('Graduation Year', choices=[
        (2023, '2023'),
        (2024, '2024'),
        (2025, '2025')
    ], validators=[DataRequired()])
    skills = TextAreaField('Technical Skills')
    certifications = TextAreaField('Certifications')
    projects = TextAreaField('Projects')
    submit = SubmitField('Submit Application')