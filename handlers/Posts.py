# -*- coding: utf-8 -*-
import tornado.web
from bson import ObjectId
from forms import *
from handlers import BaseHandler
import datetime


class NewTopic(BaseHandler):

    def get(self):
        form = TopicForm()
        self.view('newtopicl.html', form=form)

    def post(self):
        form = TopicForm(self.request.arguments)
        d = {}
        for k, v in form.data.items():
            d[k] = v
        d['userid'] = self.db.user.find_one({'username': self.current_user})['_id']
        if form.validate():
            self.db.Topic.insert(d)
            self.redirect('/')
        else:
            self.view('newtopicl.html', form=form)


class DetailTopic(BaseHandler):

    def get(self, _id):
        topic = self.db.Topic.find_one({'_id': ObjectId(_id)})
        comment_count = self.db.comment.find({'topic_id': ObjectId(_id)}).count()
        s = []
        for l in list(self.db.comment.find({'topic_id': ObjectId(_id)})):
            d = {}
            for k, v in l.items():
                d[k] = v
            if d['user_id']:
                d['commentator'] = self.db.user.find_one({'_id': ObjectId(d['user_id'])})['username']

            s.append(d)
        self.view('detailtopic.html', topic=topic, comment_id=s, comment_count=comment_count)


class TopicRrply(BaseHandler):

    def get(self, _id):
        topic_id = self.db.Topic.find_one({'_id': ObjectId(_id)})['_id']
        content = self.get_argument('content')
        user_id = self.db.user.find_one({'username': self.current_user})['_id']
        time = datetime.datetime.now().strftime('20%y-%m-%d')
        self.db.comment.insert({'topic_id': topic_id, 'content': content, 'user_id': user_id, 'time': time})
        self.redirect('/topic/'+_id + '/')


class DeleteTopic(BaseHandler):

    def get(self, _id):
        # topic_id = self.db.Topic.find_one({'_id': ObjectId(_id)})['_id']
        userid = self.db.Topic.find_one({'_id': ObjectId(_id)})['userid']
        user_id = self.db.user.find_one({'username': self.current_user})['_id']
        print user_id, userid
        if userid == user_id:
            self.db.Topic.remove({'_id': ObjectId(_id)})
            self.redirect('/member/'+_id)
        else:
            self.view('401.html')


