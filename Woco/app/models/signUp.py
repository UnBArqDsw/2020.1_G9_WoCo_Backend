from ..db.database import db


class SignUp(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created = db.Column(db.DateTime, nullable = False, default = datetime.datetime.utcnow)