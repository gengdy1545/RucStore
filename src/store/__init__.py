from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = r"mysql://username:password@127.0.0.1:3306/database"
app.config['SECRET_KEY'] = 'secret_key'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manage = LoginManager(app)
login_manage.login_view = "login"
login_manage.login_message_category ="info"

from store import routes