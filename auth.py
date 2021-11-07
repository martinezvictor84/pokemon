from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
from datetime import datetime, timedelta
from functools import wraps
from models import Users
from database import db_session
from flask import current_app

bp = Blueprint('auth', __name__)


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return jsonify({'message': 'a valid token is missing'}), 401
        try:
            data = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms='HS256'
            )
            current_user = Users.query.filter_by(
                public_id=data['public_id']).first()
        except Exception:
            return jsonify({'message': 'token is invalid'})
        return f(current_user, *args, **kwargs)

    return decorator


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    if not (data and data.get('username') and data.get('password')):
        return jsonify({'message': 'bad request'}), 400
    user = Users.query.filter_by(name=data.get('username')).first()
    if user and check_password_hash(user.password, data.get('password')):
        token = jwt.encode(
            {
                'public_id': user.public_id,
                'exp': datetime.utcnow() + timedelta(minutes=30)
            },
            current_app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token})
    return jsonify({'message': 'could not verify'}), 401


@bp.route('/register', methods=['POST'])
def signup_user():
    data = request.get_json()
    if not (data and data.get('username') and data.get('password')):
        return jsonify({'message': 'bad request'}), 400
    hashed_password = generate_password_hash(data['password'])
    new_user = Users(public_id=str(uuid.uuid4()), name=data['username'],
                     password=hashed_password, admin=False)
    db_session.add(new_user)
    try:
        db_session.commit()
    except IntegrityError:
        return jsonify({'message': 'el usuario ya existe'}), 400
    return jsonify({'message': 'registered successfully'})

