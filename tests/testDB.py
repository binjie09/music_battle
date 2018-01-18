"""
    filename: 
    date:     
    :copyright: (c) 2017 by binjie chen.
"""

from musicapp.models import Users, Musics

# user1 = Users(
#     name='admin',
#     orange=11,
#     password='123',
#     email='binjie09@gmail.com'
# )
# user1.save()

for i in range(1, 30):
    voice = Musics(
        m_id=str(i),
        name='asd',
        rank=1200 + i * 10,
        owner='admin'
    )
    voice.save()
# users = Users.objects.all()  # 返回所有的文档对象列表
# for u in users:
#     print("name:", u.name)
