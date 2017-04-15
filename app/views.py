from app import app, models, db
from .models import *
from flask import redirect, flash, session, request, url_for, jsonify, render_template
from config import *
import json

@app.route('/')
def index():
    if 'google_token' in session:
        me = google.get('userinfo')
        if 'error' in me.data:
            return redirect(url_for('logout'))
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
        db.session.add(User(email))
        db.session.commit()
    return redirect(url_for('index'))

@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')

@app.route('/pin/create', methods=['POST'])
def create_pin():
    name = request.form['name']
    me = google.get('userinfo')
    email = me.data['email']
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
    else:
        flash("Pin not found.")
    return redirect(url_for('index'))

@app.route('/pin/<string:pin_id>')
def display_one_pin(pin_id):
    pin = Pin.query.filter_by(id=pin_id).first()
    if pin:
        lat_input = pin.lat
        lng_input = pin.lng
        latLng_input = True
    else:
        flash("Pin not found.")
    return render_template('index.html.j2', lat=lat_input,
                                            lng = lng_input,
                                            latLng_inputted = latLng_input)

@app.route('/user/<string:email>')
def display_users_pins(email):
    user = User.query.filter_by(email=email).first()
    pins = None
    if user:
        pins = Pin.query.filter_by(user_id = user.id).all()
        if len(pins) == 0:
            flash("No pins found for this user.")
    else:
        flash("User not found.")
    return render_template('index.html.j2', pins=pins, user=user)
