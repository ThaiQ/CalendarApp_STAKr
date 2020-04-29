from src import app
from src import db
from flask import render_template, redirect ,
from src.forms import RegistrationForm,DeleteAccountForm
from src.schemas import User

@app.route('/register', methods=['GET', 'POST'])
def reg():
    form = RegistrationForm()
    delete_acc_form = DeleteAccountForm(request.form)

if request.method =='POST'  :	
		if 'Delete Account' == request.form['submit']:			
			db.session.delete(current_user)
			db.session.commit()
			print("Deleting account")
			return redirect(url_for('login'))

 return render_template('register.html', form=form)