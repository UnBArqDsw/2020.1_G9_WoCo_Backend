from flask import Blueprint, jsonify, request
from flask import Flask
import sqlalchemy
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import *
from ..db.database import db
from sqlalchemy.sql import exists
from ..models.signUp import SignUp



def Login(blueprintName: str):

    blueprint = Blueprint(blueprintName, __name__)
    @blueprint.route('/api/token', methods = ["POST"])
    def LoginVerification():
    
        email = request.json.get('email', None)
        password = request.json.get('password', None)

        user = db.session.query(SignUp).filter_by(email=str(email), password=str(password)).first()

        if(user is not None):
            access_token = create_access_token(identity=email)
            return jsonify(access_token=access_token, email=str(email), username=str(user.username)), 200
        else:
            return jsonify("User Not Found"), 404


    return blueprint

blueprint = Login('login')
