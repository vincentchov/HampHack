from app import app, models
from models import *

@app.route('/')
def index():
    return "Hello world, and all who inhabit it!"

