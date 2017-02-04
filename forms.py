# -*- coding: utf-8 -*-

from wtforms import StringField, validators, PasswordField, DateTimeField
from wtforms.validators import EqualTo, Required
from wtforms_tornado import Form


class UserForm(Form):
    username = StringField('username', validators=[validators.length(min=4, max=25, message=u'请输入4-25个字符')],
                           default=u'test')
    email = StringField('Email', validators=[
        validators.length(min=6, message=u'请输入有效的邮箱地址'),
        validators.Email(message=u'请输入有效的邮箱地址')])
    password = PasswordField('New Password', validators=[validators.length(min=6, max=20, message=u'请输入6-20位密码')])
    confirm = PasswordField('Repeat Password', validators=[EqualTo('password', message=u'密码不一致')])
    mobile = StringField('Mobile', validators=[validators.length(min=11, max=11, message=u'请输入11位数,并以1开头')])


class TopicForm(Form):
    userid = StringField('userid')
    title = StringField('title', validators=[Required()])
    context = StringField('context')
    flag = StringField('flag')
    node = StringField('node')


class CountersForm(Form):
    _id = StringField('_id')
    seq = StringField('seq')


class CommentForm(Form):
    Content = StringField('content', validators=[Required()])
    Topic_id = StringField('topic_id')
    User_id = StringField('user_id')
    time = DateTimeField('time')


class TagForm(Form):
    tag = StringField('tag')
    tag_name = StringField('tag_name')


