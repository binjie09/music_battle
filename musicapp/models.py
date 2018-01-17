"""
    filename: 
    date:     
    :copyright: (c) 2017 by binjie chen.
"""
import pymongo
from mongoengine import *
import datetime

connect('test', host='localhost', port=27017)


class User(Document):  # 用户类->继承自mongoengine的Document类，使用对象文档映射器来更好的MVC
    name = StringField(required=True, max_length=200)
    email = StringField(required=True)

    def __init__(self, name, email):  # 构造函数
        self.name = name
        self.email = email

    def save(self):  # 保存到数据库
        pass

    @staticmethod
    def query_users(flag, username):  # 查询用户的静态方法，如果flag为1则查询所有用户
        if flag == 1:
            return
        else:
            return

    def get_music(self):  # 获取该用户的所有音乐 返回值为一个collection
        pass

    @staticmethod
    def battle(user_a, user_b):  # 两个用户评分
        pass

    def dian_zan(self):  # 给该用户点赞
        pass


class Contest(Document):  # 比赛类

    def __init__(self):
        pass


class Music(Document):  # 音乐角色类
    id = StringField(required=True)
    rank = IntField(required=True)
    owner = StringField(required=True)