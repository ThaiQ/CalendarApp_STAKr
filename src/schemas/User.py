from src import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    """user's unique id"""
    username = db.Column(db.String(64), index=True, unique=True)
    """user's username"""
    email = db.Column(db.String(128), index=True, unique=True)
    """user's email"""
    password_hash = db.Column(db.String(128))
    """hashed version of user's password"""

    def set_password(self, password):
        """
        Set password for user

            Hash the password parameter and set the user's password_hash

        Parameters:
            password (str):
                user's password
        """
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
