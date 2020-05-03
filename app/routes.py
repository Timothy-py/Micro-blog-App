from app import appInstance
from flask import render_template, redirect, flash, url_for, request
from .forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from .models import User
from werkzeug.urls import url_parse
from .models import Post


@appInstance.route('/index')
@appInstance.route('/')
@login_required
def index():

    return render_template('index.html', title='Home', posts=Post)


@appInstance.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    else:
        form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(nickname=form.username.data).first()
        print(user)
        if user is None or not user.check_password(form.password.data):
            print(form.password.data)
            flash("Invalid username or password")
            return redirect(url_for('login'))
        else:
            login_user(user=user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@appInstance.route('/logout',)
def logout():
    logout_user()
    return redirect(url_for('index'))
