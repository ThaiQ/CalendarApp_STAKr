from flask import render_template
from flask import redirect
from flask import flash
from src import app
from src.forms import LoginForm

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
    current_form = LoginForm()
    if current_form.validate_on_submit():
        flash(f'Login requested for user {current_form.username.data}')
        return redirect('/')
    return render_template('Login/login.html', title='Sign In', form=current_form)