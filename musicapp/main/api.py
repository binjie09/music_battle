"""
    filename: 
    date:     
    :copyright: (c) 2017 by binjie chen.
"""

from flask import render_template, redirect, url_for
#导入蓝本 main
from flask import request
from . import main


@main.route('/login', methods=['POST'])  # 登录接口
def do_login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error = error)


@main.route('/register', methods=['POST'])  # 注册接口
def do_register(register):
    pass


# 登录验证操作
def valid_login(username, password):
    if username is 'admin' and password is '1':
        return True
    return False


# 登录后的操作
def log_the_user_in(username):
    return '欢迎你' + username




