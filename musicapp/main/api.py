"""
    filename: 
    date:     
    :copyright: (c) 2017 by binjie chen.
"""

from flask import render_template, redirect, url_for, flash
# 导入蓝本 main
from flask import request
from . import main
from musicapp.models import Users
from flask_wtf import FlaskForm
from flask_login import current_user, logout_user, login_user
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length


class NameForm(FlaskForm):
    name = StringField('what is your name?', validators=[Length(min=3, max=10, message=u"用户名长度有问题")])
    password = PasswordField('what is your password?', validators=[Length(min=1, max=20)])
    login = SubmitField('login')
    logout = SubmitField('logout')


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = NameForm()
    # user=Users.query_users(1, form.name.data).first()
    user = Users.query_users(1, form.name.data).first()
    if form.validate_on_submit():
        if user is not None and valid_login(user.name, form.password.data):
            if current_user.is_authenticated:
                logout_user()
                flash('User Logout')
            else:
                login_user(user, True)
                flash('User Login Success' + user.password)
    return render_template('login.html', form=form)


@main.route('/register', methods=['POST'])  # 注册接口
def do_register(register):
    pass


# 登录验证操作
def valid_login(username, password):
    tmp = Users.objects(name=username)
    for u in tmp:
        if u.password == password:
            print("dengluchengg")
            return True


# 登录后的操作
def log_the_user_in(username):
    return '欢迎你' + username
