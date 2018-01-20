"""
    filename: 
    date:     
    :copyright: (c) 2017 by binjie chen.
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from musicapp.models import Users

# Managing user login
login_manger = LoginManager()
# Protect user login, use 'strong' can make user logout if ip is change.
login_manger.session_protection = 'strong'
# The login view, if user use a url need a login session, redirect to it.
login_manger.login_view = 'main.login'
# Login message
login_manger.login_message = u'对不起，您还没有登录'
login_manger.login_message_category = 'info'
# upload folder path



@login_manger.user_loader  # This decorator is use to load user in Users class, need return a Users object by name
def load_user(username):
    return Users.objects(name=username).first()


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    db.init_app(app)
    login_manger.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
