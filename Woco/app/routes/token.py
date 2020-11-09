from flask import Blueprint, jsonify, request
from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import *



def tt(blueprintName: str):

    blueprint = Blueprint(blueprintName, __name__)
    @blueprint.route('/api/protected', methods = ["GET"])
    @jwt_required
    def protected():
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        #return jsonify(logged_in_as=current_user), 200
        return '%s' % current_identity

    @blueprint.route('/api/token', methods = ["POST"])
    def test():
    
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200


    return blueprint

blueprint = tt('tt')
