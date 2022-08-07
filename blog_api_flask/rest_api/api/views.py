from flask import Blueprint, request, jsonify
from rest_api.db import (
    get_views, get_view, add_views,
    update_view, reset_view
)
from flask_cors import CORS
from .tokens import authorizedToken


views_api = Blueprint(
    'views_api', 'views_api', url_prefix='/api/views')

CORS(views_api)

@views_api.route('/', methods=['GET'])
def getViews():

    views, qty = get_views()

    response = {
        "qty": qty,
        "views": views
    }

    return jsonify(response)

@views_api.route('/<int:id>', methods=['GET'])
def getView(id):

    view = get_view(id)

    if not view:
        return jsonify({'message': 'Not found'})

    return jsonify(view)

@views_api.route('/', methods=['POST'])
def addViews():

    data = request.json
    
    results, ignoreds = add_views(data)
    
    return jsonify({'added': results, 'duplicated': ignoreds})


@views_api.route('/<int:id>', methods=['PATCH'])
def updateView(id):

    response = None
    result = update_view(id)

    if not result.modified_count:
        response = {'message': 'Not modified'}

    view = get_view(id)

    if not view:
        response = {'message': 'Not found'}

    if not response:
        return jsonify(view)
    else:
        return jsonify(response)

@views_api.route('/reset-view/<int:id>', methods=['PATCH'])
@authorizedToken
def resetView(id):

    response = None
    result = reset_view(id)

    if not result.modified_count:
        response = {'message': 'Not modified'}

    view = get_view(id)

    if not view:
        response = {'message': 'Not found'}

    if not response:
        return jsonify({'reset': view})
    else:
        return jsonify(response)
