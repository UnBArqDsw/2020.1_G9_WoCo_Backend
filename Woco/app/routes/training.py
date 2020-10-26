from flask import Blueprint, jsonify, request
from ..db.database import db
from ..models.training import Training
import uuid

def createTraining(blueprintName: str):
  blueprint = Blueprint(blueprintName, __name__)

  @blueprint.route('/api/training', methods = ["POST"])
  def addTraining():
    data = request.get_json()
    newTraining = Training(id = str(uuid.uuid4()), name = data["name"], instructions = data["instructions"])
    db.session.add(newTraining)
    db.session.commit()
    return jsonify(TrainingSerializer.serialise(newTraining)), 201

  @blueprint.route('/api/training', methods = ["GET"])
  def loadTraining():
    trainings = Training.query.all()
    return jsonify(TrainingSerializer.serialiseArray(trainings)), 201

  return blueprint

blueprint = createTrainingBlueprint('trainingBlueprint')