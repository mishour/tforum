# -*- coding: utf-8 -*-
from core.web import RequestHandler


class BaseHandler(RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie("username")