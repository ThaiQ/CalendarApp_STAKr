from flask import render_template
from flask import redirect
from flask import flash
from flask_login import current_user, login_user
from src import app
from src.forms import Settings
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
	"""
	if current_user.is_authenticated:
		return redirect('/')
	"""
	current_form = SettingsForm()
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
