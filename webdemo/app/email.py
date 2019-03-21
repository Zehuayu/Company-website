from app import mail
from flask_mail import Message
from flask import current_app,render_template


def send_reset_password_mail(user, token):
    msg = Message("[Flask APP] Reset Your Password",
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[user.email,],
                  html=render_template('reset_password_mail.html', user=user, token=token))
    

    mail.send(msg)