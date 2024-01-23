# auth/auth_blueprint.py
from flask import Blueprint, render_template, request, redirect, url_for, session

auth_bp = Blueprint("auth", __name__,template_folder="templates")

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Your authentication logic here (e.g., validate username and password)
        if username == 'user1' and password == 'password':
            session['user'] = {'username': username, 'is_authenticated': True}
            return redirect(url_for('blog.home'))

        else:
            error_message = 'Invalid username or password'

    return render_template('login.html', error_message="pls login")

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('blog.home'))
