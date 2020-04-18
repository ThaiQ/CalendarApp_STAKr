from flask import render_template
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
    user_dictionary = {'username': 'Miguel'}
    posts_list = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('Home/home.html', title='Home', user=user_dictionary, posts=posts_list)