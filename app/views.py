from app import app, models
from .models import *
from flask import redirect, flash, session, request, url_for, jsonify, render_template
from config import *

@app.route('/')
def index():
    if 'google_token' in session:
        me = google.get('userinfo')
        return render_template('index.html.j2')
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))

@app.route('/logout')
def logout():
    session.pop('google_token', None)
    return redirect(url_for('index'))

@app.route('/login/authorized')
def authorized():
    resp = google.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (resp['access_token'], '')
    me = google.get('userinfo')
    email = me.data['email']
    exists = User.query.filter_by(email=email).first()
    if not exists:
        db.add(User(email))
        db.commit()
    return jsonify({"data": me.data})

@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')

@app.route('/pin/create', methods=['POST'])
def create_pin():
    name = request.form['name']
    me = google.get('userinfo')
    user_id = User.query.filter_by(email=me.data['email']).first().id
    description = request.form['description']
    pin = Pin(name, user_id, description)
    db.session.add(pin)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/pin/delete', methods=['POST'])
def delete_pin():
    pin_id = int(request.form['pin_id'])
    pin = Pin.query.filter_by(id=pin_id).first()
    if pin:
        db.session.delete(pin)
        db.session.commit()
    return redirect(url_for('index'))
