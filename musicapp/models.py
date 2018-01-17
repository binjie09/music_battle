"""
    filename: 
    date:     
    :copyright: (c) 2017 by binjie chen.
"""

from mongoengine import *


connect('test', host='localhost', port=27017)


class User(Document):  # 用户类->继承自mongoengine的Document类，使用对象文档映射器来更好的MVC
    name = StringField(required=True, max_length=200)
    email = StringField(required=True)
    password = StringField(required=True)
    orange = IntField(required=True)

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
    id = StringField(required=True)
    pic = StringField(required=True)  # 比赛封面
    person_a =  StringField(required=True)
    voice_a = StringField(required=True)  # 声音文件的路径
    person_b = StringField(required=True)
    voice_b = StringField(required=True)  # 声音文件的路径
    vote_a = IntField(required=True)  # 给a投票的人数
    vote_b: IntField(required=True)  # 给b投票的人数
    start_time = StringField(required=True);


class Music(Document):  # 音乐角色类
    id = StringField(required=True)
    name = StringField(required=True)
    rank = IntField(required=True)
    owner = StringField(required=True)

    def matching(self):  # 匹配对手（放到一个匹配队列里面）每次都让队列最前端的音乐角色选择rank分和他最近的音乐角色匹配，匹配成功则出队，形成一个Contest，生成Contest对象
        pass