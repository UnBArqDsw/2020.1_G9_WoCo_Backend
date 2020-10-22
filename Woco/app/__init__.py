import os
from flask import Flask
import sqlite3
import db.database
from db.database import SqliteDB

app = Flask(__name__)

@app.route("/")
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