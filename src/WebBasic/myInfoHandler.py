#!/usr/bin/env python
# coding:utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


class myInfoHandler(tornado.web.RequestHandler):
    """ TODO: how to add a request handler? """
    def get(self):
        self.write("the info of Paul Yang")