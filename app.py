from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from helpers.database_connection import EngineConnect

app = Flask(__name__)
app.config.from_object('config.common')
CORS(app)
engine = EngineConnect()
db = SQLAlchemy(app)
BaseModel = db.Model
migrate = Migrate(app, db)

from routes import *

if __name__ == '__main__':
    app.run()
