# -*- coding: utf-8 -*-

import pymongo
from tornado.options import options


class MongoMixin(object):

    @property
    def db(self):
        if not hasattr(self, '_db'):
            self._db = pymongo.MongoClient(options.MONGO_HOST)[options.MONGO_NAME]

        return self._db


