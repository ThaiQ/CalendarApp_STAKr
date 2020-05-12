from src.schemas import User
from src import db

valid_user = {
    'username' : 'username',
    'email' : 'email',
    'start_available' : -1,
    'end_available' : -1,
    'meeting_length' : -1,
    'password': '123'
}

new_user = {
    'username' : 'new username ok?',
    'email' : 'new email ok?',
}

def test_createUser():
    user = User(username=valid_user['username'], email=valid_user['email'], 
    start_available=valid_user['start_available'], 
    end_available = valid_user['end_available'], meeting_length = valid_user['meeting_length'])
    user.set_password(valid_user['password'])
    #commit data
    db.session.add(user)
    db.session.commit()
    findUser = User.query.filter_by(username=valid_user['username']).first()
    #assert data is saved
    assert findUser.username == valid_user['username']
    assert findUser.email == valid_user['email']
    assert findUser.start_available == valid_user['start_available']
    assert findUser.end_available == valid_user['end_available']
    assert findUser.meeting_length == valid_user['meeting_length']

def test_updateUser():
    findUser = User.query.filter_by(username=valid_user['username']).first()
    findUser.username = new_user['username']
    findUser.email = new_user['email']
    db.session.commit()
    findUser = User.query.filter_by(username=new_user['username']).first()
    print(findUser)
    assert findUser.username == new_user['username']
    assert findUser.email == new_user['email']

def test_deleteUser():
    #delete user
    findUser = User.query.filter_by(username=new_user['username']).first()
    assert findUser is not None
    db.session.delete(findUser)
    db.session.commit()
    #find deleted user
    findUser = User.query.filter_by(username=new_user['username']).first()
    assert findUser is None