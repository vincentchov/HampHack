from app import app, models
from .models import *
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html.j2')
