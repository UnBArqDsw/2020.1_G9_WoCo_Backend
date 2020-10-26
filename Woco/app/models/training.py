from ..db.database import db
import datetime

class Training(db.Model):
  __tablename__ = "training"

  id = db.Column(db.String(36), primary_key = True, unique = True)
  name = db.Column(db.String(50), nullable = False)
  instructions = db.Column(db.String(200), nullable = False)
  created = db.Column(db.DateTime, nullable = False, default = datetime.datetime.utcnow)
  responsibleCoach = db.Column(db.String(50), nullable = False)
