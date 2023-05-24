from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS


from .config import SQLALCHEMY_DATABASE_URI
from .models import db, init_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI#'sqlite:////tmp/demo.db'

db.init_app(app)  # 关联app和db
init_db(app)
jwt = JWTManager(app)
CORS(app)