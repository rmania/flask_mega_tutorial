from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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

@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    # gather all data, run all validators attached to fields, if ok return
    # True, indicating that data is valid and can be processed by the app
    # flashed messages will not magically appear in web pages: these are added
    # to the base.html
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)