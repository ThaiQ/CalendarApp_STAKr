from flask import render_template
from flask import redirect
from flask import flash, request
from flask_login import current_user, login_user
from src import app, db
from src.forms import SettingsForm
from src.schemas import User

@app.route('/settings', methods=['GET', 'POST'])
def settings():
	
	"""
	Settings
		Change Availability

	Parameters:
		N/A

	Returns:
		Rendered template html

	"""
	#handles if someone types in this url when already logged in
	
	if not current_user.is_authenticated:
		return redirect('/')
	
	current_form = SettingsForm()
	print("Right before if")
	if request.method == "POST":
		print("hi")
		user = User.query.filter_by(username=current_user.username).first()
		#user = User(username = current_user.username, email=current_user.email, start_available=form.start_time.data, end_available = form.end_time.data, meeting_length = form.duration.data)
		start_available= current_form.start_time.data
		end_available = current_form.end_time.data
		meeting_length = current_form.duration.data
		db.session.commit()
		user = User.query.filter_by(username=current_user.username).first()
		return str(user.start_available)
	"""
	if current_form.validate_on_submit():
		user = User.query.filter_by(username=current_form.username.data).first()
		if user is None or not user.check_password(current_form.password.data):
			flash('Invalid username or password')
			return redirect('/login')
		login_user(user, remember=current_form.remember_me.data)
		return redirect('/')
	"""
	return render_template('Settings/settings.html', title='Change Settings', form=current_form)
