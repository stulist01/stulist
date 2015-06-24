# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from dbconn import db_stulist

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("pages/main.html")


class CourseListHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("pages/cou_list.html", courses = dal_list_courses())


def dal_list_courses():
    data = []
    with db_cursor() as cur : # 取得操作数据的游标，记为cur
        s = """
        SELECT cou_sn, cou_no, name, birth, gender, class0  FROM course ORDER BY class0 
        """
        cur.execute(s)      
        for r in cur.fetchall():
            cou = dict(cou_sn=r[0], cou_no=r[1], name=r[2], birth=r[3], gender=r[4], class0=r[5])
            data.append(cou)
    print(data)
    return data

