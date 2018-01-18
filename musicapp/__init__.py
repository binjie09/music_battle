"""
    filename: 
    date:     
    :copyright: (c) 2017 by binjie chen.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager

# 用户认证
login_manger = LoginManager()
# 认证加密程度
login_manger.session_protection = 'none'
# 登陆认证的处理视图
login_manger.login_view = 'main.login'
# 登陆提示信息
login_manger.login_message = u'对不起，您还没有登录'
login_manger.login_message_category = 'info'
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    login_manger.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
