from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/projects/')
def projects():
    pageName = "projects"
    return render_template('hello.html',pageName=pageName)

@app.route('/:lureID')
def about():
    pageName = 'about'
    return render_template('about.html',pageName=pageName)

@app.route('/')
def home():
    pageName = "homme"
    return render_template('hello.html',pageName=pageName)

@app.route('/profile')
def profile():
    return render_template('profile.html')

