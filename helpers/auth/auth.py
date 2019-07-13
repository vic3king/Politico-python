import os
import bcrypt
import jwt


from functools import wraps
from flask import request, g
from graphql import GraphQLError

from api.user.models import User

secret = os.getenv('SECRET_KEY')


class Authentication:
    def decode_token(token):
        payload = jwt.decode(
            token,
            secret,
            algorithms=['HS256']
        )

        return payload

    def verify_password(password, hashed_password):
        return bcrypt.checkpw(
            password.encode('utf-8'), hashed_password.encode('utf-8')
        )

    def login_required(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if 'Authorization' not in request.headers:
                raise GraphQLError('Token not provided or is invalid.')

            user_id = None
            auth_header = request.headers.get('Authorization')
            if auth_header and len(auth_header.split(" ")) == 2:
                auth_token = auth_header.split(" ")[1]
            else:
                auth_token = ''

            try:
                user_id = User.decode_token(auth_token).get('id')
                user_type = User.decode_token(auth_token).get('user_type')

                g.user_id = user_id
                g.user_type = user_type
            except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
                raise GraphQLError('Token not provided or is invalid.')

            return fn(*args, **kwargs)

        return wrapper

    def user_roles(expected_args):
        def decorator(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                auth_header = request.headers.get('Authorization')
                auth_token = auth_header.split(" ")[1]
                user_type = User.decode_token(auth_token).get('user_type')

                if user_type in expected_args:
                    res = fn(*args, **kwargs)
                    return res
                else:
                    raise GraphQLError(
                        "You are not authorized to perform this action"
                    )

            return wrapper
        return decorator
