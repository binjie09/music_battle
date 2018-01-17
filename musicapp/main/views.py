"""
    filename: 
    date:     
    :copyright: (c) 2017 by binjie chen.
"""

from flask import render_template
# 导入蓝本 main
from flask import request
from . import main


@main.route('/')  # 主页面
def index():
    return render_template('index.html',title = '首页')


@main.route('/login')  # 登录界面
def login():
    return render_template('login.html', title = '登录')


@main.route('/register')  # 注册界面
def register():
    return render_template('register.html', title = '注册')


@main.route('/rank')  # 排名界面
def rank():
    return render_template('rank.html', title = '排行榜')


@main.route('/<musicid>')  # 音乐打分界面
def music(musicid):
    return render_template('media.html', title = '裁判')