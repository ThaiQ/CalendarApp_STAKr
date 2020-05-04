from flask import render_template
from flask import redirect
from flask import flash, request
from flask_login import current_user, logout_user
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
	if request.method == "POST":
		user = User.query.filter_by(username=current_user.username).first()
		if request.form['submit_button'] == 'Save Changes':			
			#if user submits, updates database with times
			print(f'{current_form.start_time.data} {current_form.end_time.data} {current_form.start_time.data < current_form.end_time.data}')
			if(current_form.start_time.data < current_form.end_time.data):
				user.start_available = current_form.start_time.data
				user.end_available = current_form.end_time.data
				user.meeting_length = current_form.duration.data
				db.session.commit()
				flash ("Settings saved!")
			else:
				flash("Start Time must be before End Time")
		elif request.form['submit_button'] == 'Delete Account':
			logout_user()
			db.session.delete(user)
			db.session.commit()
			return redirect('/')
	return render_template('Settings/settings.html', title='Change Settings', form=current_form)
