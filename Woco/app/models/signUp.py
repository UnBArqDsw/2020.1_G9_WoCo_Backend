from ..db.database import db
import datetime


class SignUp(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(36), primary_key = True, unique = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100))
    created = db.Column(db.DateTime, nullable = False, default = datetime.datetime.utcnow)