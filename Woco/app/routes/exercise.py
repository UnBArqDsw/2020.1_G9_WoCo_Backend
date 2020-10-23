from flask import Blueprint, jsonify, request
from ..db.database import db
from ..models.execise import Exercise
from ..serialisers.exerciseSerialiser import ExerciseSerializer
import uuid

def createExerciseBlueprint(blueprintName: str):
  blueprint = Blueprint(blueprintName, __name__)

  @blueprint.route('/api/exercise', methods = ["POST"])
  def addExercise():
    data = request.get_json()
    newExercise = Exercise(id = str(uuid.uuid4()), name = data["name"], instructions = data["instructions"])
    db.session.add(newExercise)
    db.session.commit()
    return jsonify(ExerciseSerializer.serialise(newExercise)), 201

  @blueprint.route('/api/exercise', methods = ["GET"])
  def loadExercises():
    exercises = Exercise.query.all()
    return jsonify(ExerciseSerializer.serialiseArray(exercises)), 201

  return blueprint

blueprint = createExerciseBlueprint('exerciseBlueprint')