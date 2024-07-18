from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///erp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from models import Funcionario

@login_manager.user_loader
def load_user(user_id):
    return Funcionario.query.get(int(user_id))

if __name__ == '__main__':
    from routes import *
    app.run(debug=True)