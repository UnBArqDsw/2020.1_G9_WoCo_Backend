import os
from flask import Flask
from flask_cors import CORS
from .db.database import db
from .routes.exercise import blueprint as ExerciseRoutes
from .routes.signUp import blueprint as SignUp
from .routes.token import blueprint as Token
from flask_jwt import JWT, jwt_required, current_identity
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE')
# initialize db with the flask app
db.init_app(app)

with app.app_context():
  db.create_all()

# register blueprints or routes
app.register_blueprint(ExerciseRoutes)
app.register_blueprint(SignUp)
app.register_blueprint(Token)
app.debug = True
app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']
app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['JWT_BLACKLIST_ENABLED'] = True
jwt = JWTManager(app)


if __name__ == "__main__":
  # app = createApp(os.getenv('DATABASE', 'repo/db/sqlite.db')) 
  app.run("0.0.0.0", port = 5000, debug = True)

