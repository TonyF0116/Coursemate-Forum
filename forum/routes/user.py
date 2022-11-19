from flask import flash, redirect, render_template, request, Blueprint, url_for, session
from ..models import authentication


bp = Blueprint('user', __name__, url_prefix='/user/')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        message = None

        if not username:
            message = 'Username is required.'
        elif not password:
            message = 'Password is required.'
        else:
            all_users = authentication.list_all_account()
            username_exist = False
            for user in all_users:
                if username == user.username:
                    username_exist = True
            if username_exist:
                message = 'Username exists.'
            else:
                authentication.create_user(username, password)
                return redirect(url_for('user.login'))

        flash(message)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        message = None

        if not username:
            message = 'Username is required.'
        elif not password:
            message = 'Password is required.'
        else:
            message = authentication.check_password(username, password)

            if message != "Username doesn't exist." and message != "Password incorrect.":
                session.clear()
                session['user_id'] = message.username
                return redirect(url_for('index.index'))

        flash(message)

    return render_template('auth/login.html')


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index.index'))


@bp.route('/clean')
def clean():
    return authentication.delete_all_account()


@bp.route('/list')
def list():
    users = authentication.list_all_account()
    user_list = []
    for user in users:
        user_list.append(user.username)
    return user_list
