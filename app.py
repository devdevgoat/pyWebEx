from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/')
def home():
    return render_template('hello.html')