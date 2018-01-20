"""
    filename: 
    date:     
    :copyright: (c) 2017 by binjie chen.
"""
import os
from flask import Flask, request, redirect, url_for, flash, render_template
from . import main
from flask_login import current_user, logout_user, login_user, login_required
from musicapp.models import Musics, Users
import datetime

# allow user upload file's extension
ALLOWED_EXTENSIONS = set(['mp3'])
UPLOAD_FOLDER = '/Users/binjie09/PycharmProjects/untitled1/musicapp/static/media'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@main.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    if not 'file' in request.files:  # check if file is none
        flash('请上传文件，并给音乐命名')
        return render_template('uploadmusic.html',title='上传')

    if request.method == 'POST':
        file = request.files['file']
        if request.form['music_name'] == '':
            flash('必须输入一个名字')
        if file and allowed_file(file.filename):
            music_id = str(datetime.datetime.timestamp(datetime.datetime.today()))
            filename = music_id + '.mp3'
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            music = Musics(m_id=music_id, name=request.form['music_name'], rank=1200, owner=current_user.name)
            music.save()
            flash('上传成功')
        else:
            flash('现在只能上传MP3格式的音乐')


    return render_template('uploadmusic.html', title='上传')

    m_id = StringField(required=True)  # m_id is the timestamp and also is the file name of music in static folder
    name = StringField(required=True)  # music's name
    rank = IntField(required=True)  # t
    owner = StringField(required=True)
