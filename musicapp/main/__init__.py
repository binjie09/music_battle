"""
    filename: 
    date:     
    :copyright: (c) 2017 by binjie chen.
"""
from flask import Blueprint
from . import views, errors, api

# 实例化 Blueprint 类，两个参数分别为蓝本的名字和蓝本所在包或模块，第二个通常填 __name__ 即可
main = Blueprint('main', __name__)

