import datetime
import re
import requests
import json
from urllib.parse import urlparse
from collections import Counter, defaultdict
from sqlalchemy import func
from flask import Flask, jsonify, request, g
from backend import app, db
from backend.models import User
from backend.match import get_recommendations_by_shape

from .views import token_auth

# /apiv2/auth/

@app.route('/apiv2/auth/facebooklogin/', methods=['POST'])
def post_auth_facebooklogin():
    accessToken = request.json.get('accessToken')
    payload = {
        'fields': 'id,name,email',
        'pretty': 0,
        'suppress_http_code': 1,
        'access_token': accessToken
    }
    response = requests.get(
        'https://graph.facebook.com/v5.0/me', params=payload)
    json_data = json.loads(response.text)
    if 'id' not in json_data:
        return jsonify({
            'status': 'error',
            'message': 'Error trying to log you in with your facebook account.'
        }), 400
    provider_id = 'facebook$' + json_data['id']
    user = User.query.filter_by(provider_id=provider_id).first()
    if not user:
        return jsonify({
            'status': 'error',
            'message': 'No user found.'
        }), 400
    if user and 'facebook' in user.provider_id:
        user.date_last_login = datetime.datetime.now()
        db.session.commit()
        token = user.get_token()
        return jsonify({
            'status': 'success',
            'username': user.username,
            'token': token,
        })

@app.route('/apiv2/auth/facebookregister/', methods=['POST'])
def post_auth_facebookregister():
    invalid_form = False
    registration_error = ''

    accessToken = request.json.get('accessToken')
    payload = {
        'fields': 'id,name,email',
        'pretty': 0,
        'suppress_http_code': 1,
        'access_token': accessToken
    }
    response = requests.get(
        'https://graph.facebook.com/v5.0/me', params=payload)
    json_data = json.loads(response.text)

    if 'id' not in json_data:
        return jsonify({
            'status': 'error',
            'message': 'Error trying to register you in with your facebook account.'
        }), 400
    provider_id = 'facebook$' + json_data['id']

    if 'email' not in json_data or 'name' not in json_data:
        registration_error = "We're sorry your Facebook account is not associated with an email address. We cannot register you with Facebook. Please sign up for a SizeSquirrel account by filling out the Register form below and hitting the 'Register' button."

        return jsonify({
            'status': 'error',
            'message': registration_error
        }), 400
    else:
        username = json_data['email'].split('@')[0]
        email = json_data['email']
        name = json_data['name']

    existingUser = User.query.filter_by(provider_id=provider_id).first()

    # register
    if not existingUser:
        if User.query.filter(func.lower(User.username) == username.lower()).first() is not None:
            registration_error = "Username already exists."
            invalid_form = True
        if User.query.filter_by(email=email).first() is not None:
            registration_error = "A user with this email already exists."
            invalid_form = True
        if invalid_form is True:
            return jsonify({
                'status': 'error',
                'message': registration_error
            }), 400

        user = User(provider_id=provider_id, username=username, email=email, name=name,
                    date_created=datetime.datetime.now(), date_last_login=datetime.datetime.now())
        db.session.add(user)
        db.session.commit()
        token = user.get_token()
        return jsonify({
            'status': 'success',
            'username': user.username,
            'token': token,
        })
    # user already exists
    if existingUser:
        existingUser.date_last_login = datetime.datetime.now()
        db.session.commit()
        token = existingUser.get_token()
        return jsonify({
            'status': 'success',
            'username': existingUser.username,
            'token': token,
        })

@app.route("/apiv2/auth/login/", methods=["POST"])
def post_auth_login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter(func.lower(User.username)
                             == username.lower()).first()
    # If we found a user based on username then compare that the submitted
    # password matches the password in the database.  The password is stored
    # is a slated hash format, so you must hash the password before comparing
    # it.
    if user is None:
        return jsonify({
            'status': 'error',
            'message': 'Invalid username or password.'
        }), 401
    if 'sizesquirrel' in user.provider_id:
        if user and password and user.verify_password(password):
            user.date_last_login = datetime.datetime.now()
            db.session.commit()
            token = user.get_token()
            return jsonify({
                'status': 'success',
                'username': user.username,
                'token': token,
            })
        return jsonify({
            'status': 'error',
            'message': 'Invalid username or password.'
        }), 401
    else:
        return jsonify({
            'status': 'error',
            'message': 'You signed up for an account with Facebook. Please use the \'Log In Using Facebook\' button'
        }), 400

@app.route('/apiv2/auth/logout/', methods=["GET"])
def get_auth_logout():
    g.current_user = None
    return jsonify({
        'status': 'success',
        'message': 'User logged out'
    })

@app.route("/apiv2/auth/register/", methods=["POST"])
def post_auth_register():
    invalid_form = False
    registration_errors = {}
    registration_errors['email'] = ''
    registration_errors['username'] = ''
    registration_errors['password'] = ''
    registration_errors['firstName'] = ''
    registration_errors['lastName'] = ''
    
    username = request.json.get('username')
    password = request.json.get('password')
    confirmPassword = request.json.get('confirmPassword')
    email = request.json.get('email')
    firstName = request.json.get('firstName')
    lastName = request.json.get('lastName')
    provider_id = 'sizesquirrel$' + email

    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        registration_errors["email"] = "Invalid email address."
        invalid_form = True
    if not re.match(r"^[a-zA-Z0-9]+$", username):
        registration_errors["username"] = "Invalid username - Username must only contain letters or numbers."
        invalid_form = True
    if len(username) < 3:
        registration_errors["username"] = "Invalid username - Username must be at least 3 characters."
        invalid_form = True
    if confirmPassword != password:
        registration_errors["password"] = "Invalid password - Passwords do not match."
        invalid_form = True
    if ' ' in password:
        registration_errors["password"] = "Invalid password - Password must not contain any spaces."
        invalid_form = True
    if len(password) < 6:
        registration_errors["password"] = "Password must be at least 6 characters long."
        invalid_form = True
    if username == "" or username is None:
        registration_errors["username"] = "This field is required."
        invalid_form = True
    if password == "" or password is None:
        registration_errors["password"] = "This field is required."
        invalid_form = True
    if email == "" or email is None:
        registration_errors["email"] = "This field is required."  
        invalid_form = True
    if firstName == "" or firstName is None:
        registration_errors["firstName"] = "This field is required."
        invalid_form = True
    if lastName == "" or lastName is None:
        registration_errors["lastName"] = "This field is required."        
        invalid_form = True
    if User.query.filter(func.lower(User.username) == username.lower() ).first() is not None:
        registration_errors["username"] = "Username already exists."
        invalid_form = True
    if User.query.filter_by(email = email).first() is not None:
        registration_errors["email"] = "A user with this email already exists."
        invalid_form = True

    if invalid_form is True:
        return jsonify({
            'status': 'error',
            'message': registration_errors
        }), 400
    else:
        name = firstName + ' ' + lastName

    user = User(username = username, email = email, provider_id = provider_id, name = name, date_created=datetime.datetime.now(), date_last_login=datetime.datetime.now())
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    token = user.get_token()
    return jsonify({
        'status': 'success',
        'username': user.username,
        'token': token,
    })

@app.route('/apiv2/auth/token/', methods=['GET'])
@token_auth.login_required
def get_auth_token():
    token = token_auth.current_user().get_token()
    return jsonify({'token': token})

@app.route('/apiv2/auth/user/', methods=['GET'])
@token_auth.login_required
def get_auth_user():
    user = token_auth.current_user().serialize_private()
    responseObject = {
        'user': user
    }
    responseObject['user']['recommendations_by_shape'] = get_recommendations_by_shape(user['id'], user['foot_shape'])

    return jsonify(responseObject)
