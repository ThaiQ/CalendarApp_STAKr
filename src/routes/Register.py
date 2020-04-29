from src import app, db, mail, serializer, salt
from flask import render_template, redirect, url_for, jsonify
from flask_login import current_user
from flask_mail import Message
from src.forms import RegistrationForm
from src.schemas import User
from itsdangerous import SignatureExpired, BadSignature

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Register.
        Collect user's input and create an account
        Then generate a token from the email
        Then send the email to user for confirmation

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
        #add user
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        #generate token
        token = serializer.dumps(form.email.data, salt = salt)
        #generate and send email
        msg = Message('Confirm Email', 
        sender='testcalendar131@gmail.com', 
        recipients=[form.email.data])
        link = url_for('email_confirmation', token=token, _external=True)
        msg.body = 'Your link is: {}'.format(link)
        mail.send(msg)
        #prompt the user to check their email
        return "Check for email confirmation"
    return render_template('Register/register.html', form=form)

@app.route('/email_confirmation/<token>')
def email_confirmation(token):
    """
    Confirming email.
        confirm user's email when direct to the link
        Return false if the token is invalid for any reason

    Parameters:
        token of the email to confirm

    Returns:
        Rendered template html
    """
    try:
        email = serializer.loads(token, salt = salt, max_age=3600)
        user = User.query.filter_by(email=email).first()
        if user is not None:
            user.email_confirmation = True
            db.session.commit()
            return 'Email confirmed!'
    except SignatureExpired:
        return 'Token expired'
    except BadSignature:
        return 'Token does not exist'
    return 'Could not confirm email'
