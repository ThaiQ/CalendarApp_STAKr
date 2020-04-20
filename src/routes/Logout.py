from flask import render_template
from flask import redirect
from flask_login import current_user, logout_user
from src import app
from src.forms import LoginForm
from src.schemas import User

    
@app.route('/logout')
def logout():
    '''
    Logout
        Logs the user out of the site
    
    Parameters:
        N/A
        
    Returns:
        Redirects user to Home page
    '''
    logout_user()
    return redirect('/')
