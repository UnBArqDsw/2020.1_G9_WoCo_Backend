import os
from flask import Flask
from .db.database import db
from .routes.exercise import blueprint as ExerciseRoutes

app = Flask(__name__)
app.config['SQLALCHEMY_DB_URI'] = os.getenv('DATABASE')
# initialize db with the flask app
db.init_app(app)

with app.app_context():
  db.create_all()

# register blueprints or routes
app.register_blueprint(ExerciseRoutes)

if __name__ == "__main__":
  # app = createApp(os.getenv('DATABASE', 'repo/db/sqlite.db')) 
  app.run("0.0.0.0", port = 5000, debug = True)
