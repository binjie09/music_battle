"""
    filename: 
    date:     
    :copyright: (c) 2017 by binjie chen.
"""

from flask import render_template, redirect, url_for, flash
from . import main
from musicapp.models import Users
from flask_wtf import FlaskForm
from flask_login import current_user, logout_user, login_user, login_required
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length


class NameForm(FlaskForm):
    """This is a form use for login view"""
    name = StringField('what is your name?', validators=[Length(min=3, max=10, message=u"用户名长度有问题")])
    password = PasswordField('what is your password?', validators=[Length(min=1, max=20)])
    login = SubmitField('login')
    logout = SubmitField('logout')


@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_anonymous is False:
        return render_template('userCenter.html', title=current_user.name)

    form = NameForm()
    # user=Users.query_users(1, form.name.data).first()
    user = Users.objects(name=form.name.data).first()
    if form.validate_on_submit():
        if user is not None and user.confirm_password(form.password.data):
            if current_user.is_authenticated:
                logout_user()
                flash('User Logout')
            else:
                login_user(user, True)
                flash('User Login Success' + user.password)
    return render_template('login.html', form=form, title='登录')


@main.route('/register', methods=['POST'])
def do_register(register):
    """register post interface need impl"""
    pass


def valid_login(username, password):
    """Input user's username and password"""
    tmp = Users.objects(name=username)
    for u in tmp:
        if u.password == password:
            print("成功登录：" + username)
            return True


@main.route('/vote', methods=['GET', 'POST'])
@login_required
def vote():
    return render_template('media.html', title='随机')


@main.route('/logout')
def logout():
    logout_user()
    return '成功注销'
