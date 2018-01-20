"""
    filename: 
    date:     
    :copyright: (c) 2017 by binjie chen.
"""

from musicapp.models import Contest, Musics
va = Musics.objects(m_id='1').first()
vb = Musics.objects(m_id='26').first()
print(va.rank)
print(vb.rank)
va.rank = Contest.battle(va.m_id,vb.m_id, 1)
vb.rank = Contest.battle(vb.m_id,va.m_id, 0)
va.save()
vb.save()
print(va.rank)
print(vb.rank)
