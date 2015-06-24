# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

import reqs



handlers = [
    (r"/coulist", reqs.CourseListHandler),
    (r"/couedit/(\d+|new)", reqs.CourseEditHandler),
    (r"/coudel/(\d+)", reqs.CourseDelHandler),
    (r"/", reqs.MainHandler),
]
application = tornado.web.Application(handlers, debug=True)
application.listen(8888)

if __name__ == '__main__':
    import ioloop
    ioloop.run() # 服务主调度
