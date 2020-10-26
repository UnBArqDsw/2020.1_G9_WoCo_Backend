from flask import Blueprint, jsonify, request
from ..db.database import db
from ..models.signUp import SignUp
from ..serialisers.signUpSerialiser import SignUpSerializer
import uuid


def createUserBlueprint(blueprintName: str):
    blueprint = Blueprint(blueprintName, __name__)

    @blueprint.route('/api/user', methods = ["POST"])
    def addUser():
        data = request.get_json()
        
        newUser = SignUp(id = str(uuid.uuid4()), username = data["username"], email = data["email"], password = data["password"])
        
        db.session.add(newUser)
        db.session.commit()
        return jsonify(SignUpSerializer.serialise(newUser)), 201

    @blueprint.route('/api/user', methods = ["GET"])
    def loadUsers():
        users = SignUp.query.all()
        return jsonify(SignUpSerializer.serialiseArray(users)), 201

    return blueprint

blueprint = createUserBlueprint('userBlueprint')
