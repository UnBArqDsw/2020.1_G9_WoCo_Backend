import os
from flask import Flask
import sqlite3
import db.database
# from db.database import SqliteDB
from db.database import db

def createApp(dbUri: str) -> Flask:
  app = Flask(__name__)
  app.config['SQLALCHEMY_DB_URI'] = dbUri
  # initialize db with the flask app
  db.init_app(app)

  # register blueprints or routes
  with app.app_context():
    db.create_all()

  return app

app = createApp('')

@app.route('/', methods = ["GET"])
def home():
    databaseUri = os.getenv('DATABASE', '/repo/db/sqlite.db')
    conn = SqliteDB(databaseUri)
    conn.execute('select sqlite_version();')
    ret = conn.cursor.fetchall()
    conn.close()
    return '''
        <html>
            <head>
                <title>Flask Proto</title>
            </head>
            <body>
                <h1>Hello World!</h1>
                <p>SQLite version: %s</p>
            </body>
        </html>
    ''' % ret[0][0]

@app.route('/', methods = ["POST"])
def addExercise():
  databaseUri = os.getenv('DATABASE', '/repo/db/sqlite.db')
  conn = SqliteDB(databaseUri)
  cursor = conn.cursor
  name = "Exercício 1"
  query1 = "INSERT INTO Exercises VALUES('{n}')".format(n = name)
  cursor.execute(query1)
  conn.commit()
  conn.close()
  