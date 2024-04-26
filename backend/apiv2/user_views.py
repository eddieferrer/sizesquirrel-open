import re
from sqlalchemy import func
from flask import jsonify, abort, request, g, current_app, render_template
from backend import app, db
from backend.emails import send_email
from backend.models import User, User_Item
from backend.utils import convert_shoe_size_to_inches
from backend.match import get_shoe_buddies, get_best_shoe_buddies


from .views import token_auth

# /apiv2/user/

@app.route('/apiv2/user/changepassword/', methods=['POST'])
@token_auth.login_required
def post_user_change_password():
    invalid_form = False

    error_current_password = ''
    error_new_password_confirm = ''

    current_password = request.json.get('currentPassword')
    new_password = request.json.get('newPassword')
    new_password_confirm = request.json.get('newPasswordConfirm')

    # user wants to change password
    if g.current_user and g.current_user.verify_password(current_password):
        if new_password != '' and new_password_confirm != '':
            if new_password != new_password_confirm:
                error_new_password_confirm = "Invalid password - Passwords do not match."
                invalid_form = True
            if ' ' in new_password:
                error_new_password_confirm = "Invalid password - Password must not contain any spaces."
                invalid_form = True
            if len(new_password) < 6:
                error_new_password_confirm = "Password must be at least 6 characters long."
                invalid_form = True
        else:
            error_new_password_confirm = "Invalid Password"
            invalid_form = True
    else:
        error_current_password = "Incorrect Password"
        invalid_form = True

    # commit changes
    if invalid_form is False:
        g.current_user.hash_password(new_password)
        db.session.add(g.current_user)
        db.session.commit()

    if invalid_form is True:
        return jsonify({
            'status': "error",
            'message': 'There was an error changing your password',
            'error_current_password': error_current_password,
            'error_new_password_confirm': error_new_password_confirm
        })

    return jsonify({
        'status': "success",
        'message': 'Password changed successfully.'
    })

@app.route('/apiv2/user/deleteaccount/', methods=["POST"])
@token_auth.login_required
def post_user_deleteaccount():
    """
    Delete User.
    """
    user_id = request.json.get('user_id')
    user = User.query.filter_by(id=user_id).first()
    if user and g.current_user == user:
        items_to_remove = User_Item.query.filter_by(user_id=int(user_id)).all()
        for item in items_to_remove:
            db.session.delete(item)
        db.session.delete(user)
        db.session.commit()

        return jsonify({
            'status': "success",
            'message': 'Account deleted successfully.',
            'new_url': '/?deleted=1'
        })
    else:
        abort(400)

@app.route('/apiv2/user/details/change/', methods=['POST'])
@token_auth.login_required
def post_user_details():
    invalid_form = False

    change_username_error = ""
    change_email_error = ""

    username = request.json.get('username')
    email = request.json.get('email')
    street_shoe_size = request.json.get('streetShoeSize')
    foot_shape = request.json.get('footShape')
    split_shoe_info = request.json.get('splitShoeInfo')
    gender = request.json.get('gender')
    climbing_boulder = request.json.get('climbingBoulder')
    climbing_sport = request.json.get('climbingSport')
    climbing_trad = request.json.get('climbingTrad')

    # user wants to change street_shoe_size
    if street_shoe_size != None and street_shoe_size != '' and street_shoe_size != 0:
        g.current_user.street_shoe_size_in = convert_shoe_size_to_inches(
            street_shoe_size)

    # foot shape, gender, and split shoe are required values
    g.current_user.foot_shape = foot_shape
    g.current_user.split_shoe_info = split_shoe_info
    g.current_user.gender = gender
    g.current_user.climbing_boulder = climbing_boulder
    g.current_user.climbing_sport = climbing_sport
    g.current_user.climbing_trad = climbing_trad

    # user wants to change username
    if g.current_user.username != username:
        if len(username) < 3:
            change_username_error = "Invalid username - Username must be at least 3 characters."
            invalid_form = True
        if not re.match(r"^[a-zA-Z0-9]+$", username):
            change_username_error = "Invalid username - Username must only contain letters or numbers."
            invalid_form = True
        # if username passes 2 test above, run db query
        if invalid_form is False:
            if User.query.filter(func.lower(User.username) == username.lower()).first() is not None:
                change_username_error = "Username already exists."
                invalid_form = True
            else:
                g.current_user.username = username

    # user wants to change email
    if g.current_user.email != email:
        if len(username) < 5:
            change_email_error = "Invalid email - Email must be at least 5 characters."
            invalid_form = True
        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
            change_email_error = "Invalid email address."
            invalid_form = True
        # if email passes 2 test above, run db query
        if invalid_form is False:
            if User.query.filter_by(email=email).first() is not None:
                invalid_form = True
                change_email_error = "A user with this email already exists."
            else:
                g.current_user.email = email

    if invalid_form is True:
        return jsonify({
            'status': "error",
            'message': 'There was an error changing your account details.',
            'username': change_username_error,
            'email': change_email_error
        })
    else:
        # make all the changes
        db.session.add(g.current_user)
        db.session.commit()
        new_url = '/profile/' + g.current_user.username + '?changed=1'
        return jsonify({
            'status': "success",
            'message': 'Account details changed successfully.',
            'new_url': new_url
        })

@app.route('/apiv2/user/details/<user_id>/', methods=['GET'])
def get_user_details(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        response = jsonify({
            'status': 'error',
            'message': 'User not found',
        })
        response.status_code = 400
        return response
    user_details = user.serialize_public()

    results = []
    user_items = User_Item.query.filter_by(user_id=user.id).all()
    for user_item in user_items:
        results.append({
            'user_item': user_item.serialize()
        })
    
    user_details["items"] = results

    return jsonify({
        'status': 'success',
        'message': '',
        'user_details': user_details
    })

@app.route('/apiv2/user/forgotusername/', methods=['POST'])
def post_user_forgotusername():
    email = request.json.get('email')
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({
            'status': 'error',
            'message': 'No user with that email address found',
        })
    else:
        if 'sizesquirrel' in user.provider_id:
            username = user.username
            # send email
            send_email("SizeSquirrel - Your SizeSquirrel Username",
                        current_app.config['ADMINS'][0],
                        [user.email],
                        render_template(
                            "emails/forgot_username.txt", username=username),
                        render_template("emails/forgot_username.html", username=username))
            return jsonify({
                'status': "success",
                'message': 'An email has been sent with your username'
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'You registered using Facebook please log in using Facebook.',
            })

@app.route('/apiv2/user/forgotpassword/', methods=['POST'])
def post_user_forgotpassword():
    email = request.json.get('email')
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({
            'status': 'error',
            'message': 'No user with that email address found',
        })
    else:
        if 'sizesquirrel' in user.provider_id:
            token = user.get_token()
            # send email
            send_email("SizeSquirrel - Reset Your Password",
                        current_app.config['ADMINS'][0],
                        [user.email],
                        render_template(
                            "emails/reset_password.txt", token=token),
                        render_template("emails/reset_password.html", token=token))
            return jsonify({
                'status': "success",
                'message': 'An email has been sent with password reset instructions'
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'You registered using Facebook and we cannot reset your password.',
            })

@app.route('/apiv2/user/items/<user_id>/', methods=['GET'])
def get_user_items(user_id):
    user = User.query.filter_by(id=user_id).first()
    results = []

    if not user:
        response = jsonify({
            'status': 'error',
            'message': 'User not found',
        })
        response.status_code = 400
        return response

    else:
        user_items = User_Item.query.filter_by(user_id=user.id).all()
        for user_item in user_items:
            results.append({
                'user_item': user_item.serialize()
            })

        return jsonify({
            'status': 'success',
            'message': '',
            'items': results
        })

@app.route('/apiv2/user/migratefb/', methods=['POST'])
def post_user_migratefb():
    email = request.json.get('email')
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({
            'status': 'error',
            'message': 'No user with that email address found',
        })
    else:
        if 'sizesquirrel' in user.provider_id:
            return jsonify({
                'status': 'error',
                'message': 'Your account is already a SizeSquirrel account. Use the log in form to log in.',
            })
        else:
            username = user.username
            # change provider_id
            user.provider_id = 'sizesquirrel$' + str(user.email)
            token = user.get_token()
            # commit db changes
            db.session.add(user)
            db.session.commit()

            # send email
            send_email("SizeSquirrel - Migrate Your Facebook Login",
                        current_app.config['ADMINS'][0],
                        [user.email],
                        render_template(
                            "emails/migrate_facebook.txt", username=username, token=token),
                        render_template("emails/migrate_facebook.html", username=username, token=token))
            return jsonify({
                'status': "success",
                'message': 'An email has been sent with instructions on how to log in with your email address.'
            })

@app.route('/apiv2/user/resetpassword/', methods=['POST'])
def post_user_resetpassword():
    token = request.json.get('token')
    password = request.json.get('password')
    confirmPassword = request.json.get('confirmPassword')

    verified_user = User.query.filter_by(token=token).first() if token else None
    if not token or not password or not confirmPassword or not verified_user:
        return jsonify({
            'status': 'error',
            'message': {
                'general': 'There was an error resetting your password, please try restarting the password reset process',
                'password': '',
                'confirmPassword': '',
            }
        })
    if confirmPassword != password:
        return jsonify({
            'status': 'error',
            'message': {
                'general': '',
                'password': 'Invalid password - Passwords do not match.',
                'confirmPassword': 'Invalid password - Passwords do not match.',
            }
        })
    if ' ' in password:
        return jsonify({
            'status': 'error',
            'message': {
                'general': '',
                'password': 'Invalid password - Password must not contain any spaces.',
                'confirmPassword': 'Invalid password - Password must not contain any spaces.',
            }
        })
    if len(password) < 6:
        return jsonify({
            'status': 'error',
            'message': {
                'general': '',
                'password': 'Invalid password - Password must be at least 6 characters long.',
                'confirmPassword': 'Invalid password - Password must be at least 6 characters long.',
            }
        })

    if verified_user:
        verified_user.hash_password(password)
        db.session.commit()
        return jsonify({
            'status': 'success',
            'message': 'Password Updated Successfully.'
        })
    else:
        abort(403)

@app.route('/apiv2/user/shoebuddies/<user_id>/', methods=['GET'])
def get_user_shoebuddies(user_id):
    return jsonify({
        'status': 'success',
        'message': '',
        'best_shoe_buddies': get_best_shoe_buddies(user_id),
        'shoe_buddies': get_shoe_buddies(user_id)
    })
