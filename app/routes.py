from app import appInstance
from flask import render_template, redirect, flash, url_for
from .forms import LoginForm


@appInstance.route('/index')
def index():
    user = {'username': 'BLOGGERS'}
    post = [
        {
            'author': {'username': 'Timothy'},
            'body': 'It\'s a brand new day!'
        },
        {
            'author': {'username': 'Obadan'},
            'body': 'It\'s a brand new Moon!'
        }
    ]
    return render_template('index.html', title='Home', user=user, post=post)


@appInstance.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for(endpoint='index'))
    return render_template('login.html', title='Sign In', form=form)

