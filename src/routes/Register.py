from src import app
from src import db
from flask import render_template, redirect, url_for
from flask_login import current_user
from flask_mail import Mail, Message
from src.forms import RegistrationForm
from src.schemas import User
from itsdangerous import TimedSerializer, SignatureExpired, BadSignature

mail = Mail (app)
serializer = TimedSerializer('serializer-secret')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Register.
        Collect user's input and create an account

    Parameters:
        N/A

    Returns:
        Rendered template html

    """
    if current_user.is_authenticated:
        #handles if someone tries to register when already logged in
        return redirect('/')
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        token = serializer.dumps(form.email.data, salt = 'email-token')
        print(token)

        msg = Message('Confirm Email', 
        sender='quachhongthai2000@gmail.com', 
        recipients=[form.email.data])
        
        link = url_for('email_confirmation', token=token, _external=True)

        msg.body = 'Your link is: {}'.format(link)
        mail.send(msg)

        return "Check for email confirmation"
    return render_template('Register/register.html', form=form)

@app.route('/email_confirmation/<token>')
def email_confirmation(token):
    try:
        email = serializer.loads(token, salt='email-token', max_age=3600)
        user = User.query.filter_by(email=email).first()
        if user is not None:
            user.email_confirmation = True
            db.session.commit()
            print(User.query.filter_by(email=email).first().email_confirmation)
            return 'the token works'
    except SignatureExpired:
        return 'Token expired'
    except BadSignature:
        return 'Token does not exist'
    return 'Could not confirm email'
