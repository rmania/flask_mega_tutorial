from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Diederik'}
    posts = [
        {
            'author': {'username': 'Arne'},
            'body' : 'Avengers Movie rocked it!'
        },
        {
            'author': {'username': 'Susanne'},
            'body': 'Waiting for Tenet!'
        }
    ]
    return render_template('index.html', title='Home',
                           user=user, posts=posts)
