from flask import Blueprint, render_template
...
@main.route('/')
def index():
    return render_template('home.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')