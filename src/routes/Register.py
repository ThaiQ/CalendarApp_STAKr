from src import app
from src import db
from flask import render_template, redirect
from src.forms import RegistrationForm
from src.schemas import User

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
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    return render_template('Register/register.html', form=form)