from flask import request, jsonify
from app.rest_api.db import get_token


def authorizedToken(func):

    def wrapper(*args, **kwargs):

        not_authorized = jsonify({'message': 'Not authorized'})

        token = get_token()

        if not token:
            return not_authorized

        try:
            header_auth = request.headers['Authorization']
            token_value = 'Bearer Token ' + token['value']
        except:
            return not_authorized
        
        if not header_auth == token_value:
            return not_authorized

        return func(*args, **kwargs)
    
    return wrapper
