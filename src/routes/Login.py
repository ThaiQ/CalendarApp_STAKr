from flask import render_template
from flask import redirect
from flask import flash
from flask_login import current_user, login_user
from src import app
from src.forms import LoginForm
from src.schemas import User

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login
        Check for valid login information

    Parameters:
        N/A

    Returns:
        Rendered template html

    """
    #handles if someone types in this url when already logged in
    if current_user.is_authenticated:
        return redirect('/')
    
    current_form = LoginForm()

    if current_form.validate_on_submit():
        user = User.query.filter_by(username=current_form.username.data).first()
        if user is None or not user.check_password(current_form.password.data):
            flash('Invalid username or password')
            return redirect('/login')
        login_user(user, remember=current_form.remember_me.data)
        return redirect('/')
    return render_template('Login/login.html', title='Sign In', form=current_form)