# -*- coding: utf-8 -*-

import tornado.web
from bson import ObjectId
from tornado.util import ObjectDict
from tornado.escape import json_encode
from core.mongo import MongoMixin


class RequestHandlerMixin(object):
    # @tornado.web.authenticated
    def view(self, template_name, **kwargs):

        kwargs['current_user'] = self.current_user
        if self.current_user:
            kwargs['id'] = self.db.user.find_one({'username': self.current_user})['_id']
            kwargs['seq_id'] = self.db.user.find_one({'username': self.current_user}).get('seq_id')

        s = []
        for l in list(self.db.Topic.find()):
            d = {}
            for k, v in l.items():
                d[k] = v
            if d['userid'] is u'':
                d['username'] = None
            else:
                username = self.db.user.find_one({'_id': d['userid']})
                d['username'] = username['username']

            s.append(d)

        kwargs['titles'] = s
        kwargs['user_count'] = self.db.user.find().count() + 4
        kwargs['topic_count'] = self.db.Topic.find().count()

        return self.render(template_name, **kwargs)


class RequestHandler(tornado.web.RequestHandler, RequestHandlerMixin):

    @property
    def db(self):
        return self.application.db


class Application(tornado.web.Application, MongoMixin, RequestHandlerMixin):

    def __init__(self, handlers=None, default_host="", transforms=None, **settings):
        print 'Application init'
        super(Application, self).__init__(handlers, default_host, transforms, **settings)

    def __call__():
        print 'Application call'
