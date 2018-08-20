from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Raymond'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Sweet Sweet Sweet!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Holy shit!'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)
