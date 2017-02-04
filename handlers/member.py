# -*- coding: utf-8 -*-
import tornado.web
from bson import ObjectId
from forms import *
from handlers import BaseHandler
import datetime


class Member(BaseHandler):

    def get(self, _id):
        user_id = ObjectId(self.db.user.find_one({'username': self.current_user})['_id'])
        topics = []
        for topic in self.db.Topic.find({'userid': user_id}):
            top = {}
            for k, v in topic.items():
                top[k] = v
            topics.append(top)

        comments = []
        for comment in self.db.comment.find({'user_id': user_id}):
            com = {}
            for k, v in comment.items():
                com[k] = v
            comments.append(com)

        print topics
        print comments
        self.view('member.html', topics=topics, comments=comments)

