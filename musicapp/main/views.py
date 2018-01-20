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


@main.route('/')
def index():
    """The index view"""
    return render_template('index.html', title='首页')


@main.route('/register')
def register():
    """The register view"""
    return render_template('register.html', title='注册')


@main.route('/rank')
def rank():
    """The rank view"""
    return render_template('rank.html', title='排行榜', musics=Musics.objects.order_by("-rank"))


@main.route('/<musicid>')
def music(musicid):
    """The music vote view"""
    return render_template('media.html', title='裁判')


@main.route('/loginrq', methods=['GET', 'POST'])
def loginrq():
    """A test login require view"""
    if current_user.is_anonymous:
        return 'is_anonymous'
    return current_user.name

@main.route('/usercenter')
@login_required
def usercenter():
    musics = Musics.objects(owner=current_user.name)
    return render_template('userCenter.html', title='个人中心',musics=musics)