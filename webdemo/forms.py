from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError



from models import User


class RegisterForm(FlaskForm):
    
    
    username = StringField('Username', validators=[DataRequired(), Length(min=6,max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8,max=20)])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    ## Recaptcha = RecaptchaField()
    submit = SubmitField('Register')


##查找数据库中是否有相同的数据 for 用户名
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Usename already taken')

## the same as before, the just different is for email

    def validate_email(self, Email):
        email = User.query.filter_by(email=Email.data).first()
        if email:
            raise ValidationError('pick one email else')

    
    
  



class LoginForm(FlaskForm):
    
    
    username = StringField('Username', validators=[DataRequired(), Length(min=6,max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8,max=20)])
    remember = BooleanField('Remember')
    submit = SubmitField('Sign In')


class PasswordResetRequestForm(FlaskForm):
   
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Send')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError("Email is exist")
       
class ResetPasswordForm(FlaskForm):
    
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8,max=20)])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    ## Recaptcha = RecaptchaField()
    submit = SubmitField('OK')
