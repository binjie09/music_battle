"""
    filename: 
    date:     
    :copyright: (c) 2017 by binjie chen.
"""

from musicapp.models import Users


user1 = Users(
    name='zz',
    orange= 11,
    password='123',
    email='binjie09@gmail.com'
)
user1.save()
print(user1.name)
user1.name = 'zz11'
user1.save()
print(user1.name)
user1.save()
users = Users.objects.all() #返回所有的文档对象列表
for u in users:
    print("name:",u.name)