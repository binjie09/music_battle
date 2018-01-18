"""
    filename: 
    date:     
    :copyright: (c) 2017 by binjie chen.
"""

from flask import render_template
# 导入蓝本 main
from . import main
from flask_login import login_required
from flask_login import current_user
from musicapp.models import Musics


@main.route('/')  # 主页面
def index():
    return render_template('index.html', title='首页')


@main.route('/register')  # 注册界面
def register():
    return render_template('register.html', title='注册')


@main.route('/rank')  # 排名界面
def rank():
    return render_template('rank.html', title='排行榜', musics=Musics.objects.order_by("-rank"))


@main.route('/<musicid>')  # 音乐打分界面
def music(musicid):
    return render_template('media.html', title='裁判')


@main.route('/loginrq', methods=['GET', 'POST'])
def loginrq():
    if current_user.is_anonymous:
        return 'is_anonymous'
    return current_user.password
