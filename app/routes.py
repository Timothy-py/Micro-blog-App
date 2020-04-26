from app import appInstance
from flask import render_template


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
