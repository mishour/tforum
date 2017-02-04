# -*- coding: utf-8 -*-
from forms import *
from handlers import BaseHandler


class Index(BaseHandler):

    def get(self):
        s = []
        if self.get_argument('tag', default=''):
            for l in list(self.db.Topic.find({'node': self.get_argument('tag')})):
                d = {}
                for k, v in l.items():
                    d[k] = v
                if d['userid'] is u'':
                    d['username'] = None
                else:
                    d['username'] = self.db.user.find_one({'_id': d['userid']})['username']
                d['tagname'] = self.db.tag.find_one({'tag': d['node']})['tag_name']
                s.append(d)

        elif self.get_argument('content', default=''):
            for l in list(self.db.Topic.find({'title': {'$regex': self.get_argument('content')}})):
                d = {}
                for k, v in l.items():
                    d[k] = v
                if d['userid'] is u'':
                    d['username'] = None
                else:
                    d['username'] = self.db.user.find_one({'_id': d['userid']})['username']
                d['tagname'] = self.db.tag.find_one({'tag': d['node']})['tag_name']
                s.append(d)
        else:
            for l in list(self.db.Topic.find()):
                d = {}
                for k, v in l.items():
                    d[k] = v
                if d['userid'] is u'':
                    d['username'] = None
                else:
                    d['username'] = self.db.user.find_one({'_id': d['userid']})['username']
                d['tagname'] = self.db.tag.find_one({'tag': d['node']})['tag_name']
                s.append(d)
        self.view('base.html',  title=s)


class Login(BaseHandler):

    def get(self):
        form = UserForm()
        self.view('login.html', form=form)

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        if self.db.user.find_one({'username': username, 'password': password}):
            self.set_secure_cookie("username", self.get_argument("username"))
            self.redirect('/')
        else:
            error = u'账号或密码错误'
            self.view('login.html', error=error)


class Logout(BaseHandler):

    def get(self):
        self.clear_cookie("username")
        self.redirect('/')


class Register(BaseHandler):

    def get(self):
        form = UserForm()
        self.view('register.html', form=form)

    def post(self):

        form = UserForm(self.request.arguments)
        if form.validate():
            def getNextSequence(name):
                ret = self.db.counters.find_one_and_update({'_id': name}, {'$inc': {'seq': 1}})
                # print ret['seq']
                return ret['seq']
            d = {}
            for k, v in form.data.items():
                d[k] = v
            d['seq_id'] = getNextSequence('userid')
            self.db.user.insert(d)
            self.view('login.html')
        else:
            self.view('register.html', form=form)

