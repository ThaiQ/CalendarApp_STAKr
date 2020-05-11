from flask import render_template, redirect
from flask_login import current_user
from src import app

@app.route("/")
def home():
    """
    Direct to homepage depending on login-credential.

    Parameters:
        N/A

    Returns:
        Rendered template html

    """
    name = {
        'thai' : 'Thai Quach',
        'khanh': 'Nguyễn Cửu Khánh',
        'alex' : 'Alex Montgomery',
        'sean' : 'Sean D. Milner'
    }
    if current_user.is_authenticated:
        return redirect('/calendar')
    return render_template('Home/home.html', title='Home', name = name)
