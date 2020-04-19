from flask import render_template
from flask_login import current_user
from src import app

@app.route("/")
def home():
    """
    Home.

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
    return render_template('Home/home.html', title='Home', posts=posts_list)