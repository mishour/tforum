# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.options
from tornado.options import define, options
from core.web import Application
import tornado.web
from handlers.index import *
from handlers.Posts import *
from handlers.member import *


define("port", default=8000, help="run on the given port", type=int)
define("MONGO_HOST", default='mongodb://127.0.0.1/tforum', help="mongo host", type=str)
define("MONGO_NAME", default='tforum', help="mongo name", type=str)


def make_app():
    settings = {
        "template_path": "templates",
        "static_path": "static",
        "debug": True,
        "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
        "xsrf_cookies": False,
    }

    return Application([
        (r"/", Index),
        (r"/login/", Login),
        (r"/logout/", Logout),
        (r"/register/", Register),
        (r"/member/(.*)", Member),
        (r"/topic/new/", NewTopic),
        (r"/topic/(.*)/reply/", TopicRrply),
        (r"/topic/delete/(.*)/", DeleteTopic),
        (r"/topic/(.*)/", DetailTopic),
        # (r"/api", Api),
    ], **settings)


if __name__ == "__main__":
    app = make_app()

    tornado.options.parse_config_file('config/default.py')
    tornado.options.parse_command_line()

    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()