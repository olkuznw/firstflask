from app import app
from flask import render_template

@app.route('/')
@app.route('/blog')
def hello_world():
    name = 'Olga K'
    return render_template('index.html')