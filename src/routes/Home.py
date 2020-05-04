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
    posts_list = [
        {
            'author': {'username': 'Alex'},
            'body': 'AMontgomery123'
        },
        {
            'author': {'username': 'Khang'},
            'body': 'khanhsjsu'
        },
		{
			'author': {'username': 'Thai'},
            'body': 'ThaiQ'
		},
		{
			'author': {'username': 'Sean'},
            'body': 'shengda419'
		}
    ]
    if current_user.is_authenticated:
        return redirect('/calendar')
    return render_template('Home/home.html', title='Home', posts=posts_list)
