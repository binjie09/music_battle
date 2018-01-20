"""
    filename: 
    date:     
    :copyright: (c) 2017 by binjie chen.
"""

from mongoengine import *
from flask_login import UserMixin

import uuid

connect('test', host='localhost', port=27017)


class Users(Document, UserMixin):
    """
        Users class extends Document for register in mongoengine
        Users class extends UserMixin for register in login_manager to manage user login
    """
    name = StringField(required=True, max_length=200)
    email = StringField(required=True)
    password = StringField(required=True)
    orange = IntField(required=True)
    zan = IntField(min_value=0)

    def get_music(self):  # 获取该用户的所有音乐 返回值为一个collection
        """get a user's musics"""
        pass

    def dian_zan(self):  # 给该用户点赞
        pass

    def confirm_password(self, passwd):  # 验证密码是否正确
        if self.password == passwd:
            return True
        return False

    def get_id(self):
        return self.name


class Contest(Document):  # 比赛类
    id = StringField(required=True)
    pic = StringField(required=True)  # Event cover pic
    person_a = StringField(required=True)
    voice_a = StringField(required=True)  # a's music id
    person_b = StringField(required=True)
    voice_b = StringField(required=True)  # b's music id
    vote_a = IntField(required=True)  # The number of votes for a
    vote_b = IntField(required=True)  # The number of votes for b
    start_time = StringField(required=True);

    # (1) P(D) = 1 / (1 + 10 ^ (-D / 400))
    # (2) D = Ra - Rb
    # (3) We = P(D1) + P(D2) + P(D3) + ... + P(Dn0) - ---连续多次比赛后的We
    # (4) Rn = Ro + K * (W - We)
    @staticmethod
    def battle(voice_a_id, voice_b_id, is_a_win):
        """Get voice_a's rank after battle with voice_b"""
        ranka = Musics.objects(m_id=voice_a_id).first().rank
        rankb = Musics.objects(m_id=voice_b_id).first().rank
        d = ranka - rankb  # (2)
        pd = 1 / (1 + 10 ** (-d / 400))  # (3)
        rn = ranka + 20 * (is_a_win - pd)  # (4)
        print('胜率可能是：%f' %(pd))
        return rn


class Musics(Document):
    """Musical character"""
    m_id = StringField(required=True)  # m_id is the timestamp and also is the file name of music in static folder
    name = StringField(required=True)  # music's name
    rank = IntField(required=True)     # t
    owner = StringField(required=True)

    def matching(self):  # 匹配对手（放到一个匹配队列里面）每次都让队列最前端的音乐角色选择rank分和他最近的音乐角色匹配，匹配成功则出队，形成一个Contest，生成Contest对象
        pass
