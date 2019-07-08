from functools import wraps
import jwt
from flask import request, g
from graphql import GraphQLError

from api.user.models import User


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
