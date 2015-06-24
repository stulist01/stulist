# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from dbconn import db_cursor

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("pages/main.html")


class CourseListHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("pages/cou_list.html", courses = dal_list_courses())

class CourseEditHandler(tornado.web.RequestHandler):
    def get(self, cou_sn):

        cou = None
        if cou_sn != 'new' :
            cou = dal_get_course(cou_sn)
        
        if cou is None:
            cou = dict(cou_sn='new', cou_no='', name='', birth='',gender='',class0='',)

        self.render("pages/cou_edit.html", course = cou)

    def post(self, cou_sn):
        cou_no = self.get_argument('cou_no')
        name = self.get_argument('name', '')
        birth = self.get_argument('birth', '')
        gender = self.get_argument('gender', '')
        class0 = self.get_argument('class0','')

        if cou_sn == 'new' :
            dal_create_course(cou_no, name, birth,gender,class0)
        else:
            dal_update_course(cou_sn,cou_no, name, birth,gender,class0)

        self.redirect('/coulist')

class CourseDelHandler(tornado.web.RequestHandler):
    def get(self, cou_sn):
        dal_del_course(cou_sn)
        self.redirect('/coulist')

# -------------------------------------------------------------------------

def dal_list_courses():
    data = []
    with db_cursor() as cur : # 取得操作数据的游标，记为cur
        s = """
        SELECT cou_sn, cou_no, name, birth,gender,class0 FROM course ORDER BY class0 
        """
        cur.execute(s)      
        for r in cur.fetchall():
            cou = dict(cou_sn=r[0], cou_no=r[1], name=r[2], birth=r[3], gender=r[4], class0=r[5])
            data.append(cou)
    return data


def dal_get_course(cou_sn):
    with db_cursor() as cur : # 取得操作数据的游标，记为cur
        s = """
        SELECT cou_sn, cou_no, name,birth,gender,class0 FROM course WHERE cou_sn=%s
        """
        cur.execute(s, (cou_sn, ))
        r = cur.fetchone()
        if r :
            return dict(cou_sn=r[0], cou_no=r[1], name=r[2], birth=r[3], gender=r[4], class0=r[5])


def dal_create_course(cou_no, name, birth,gender,class0):
    with db_cursor() as cur : # 取得操作数据的游标，记为cur
        cur.execute("SELECT nextval('seq_cou_sn')")
        cou_sn = cur.fetchone()
        assert cou_sn is not None

        print('新课程内部序号%d: ' % cou_sn)

        s = """
        INSERT INTO course (cou_sn, cou_no, name, birth,gender,class0) 
        VALUES (%(cou_sn)s, %(cou_no)s, %(name)s, %(birth)s,%(gender)s,%(class0)s)
        """
        cur.execute(s, dict(cou_sn=cou_sn, cou_no=cou_no, name=name, birth =birth,gender=gender,class0=class0))


def dal_update_course(cou_sn, cou_no, name, birth,gender,class0):
    with db_cursor() as cur : # 取得操作数据的游标，记为cur
        s = """
        UPDATE course SET
          cou_no=%(cou_no)s, 
          name=%(name)s, 
         birth= %(birth)s,
		gender= %(gender)s,
		class0=%(class0)s
        WHERE cou_sn=%(cou_sn)s
        """
        cur.execute(s, dict(cou_sn=cou_sn, cou_no=cou_no, name=name, birth =birth,gender=gender,class0=class0))


def dal_del_course(cou_sn):
    with db_cursor() as cur : # 取得操作数据的游标，记为cur
        s = """
        DELETE FROM course WHERE cou_sn=%(cou_sn)s
        """
        cur.execute(s, dict(cou_sn=cou_sn))
        print('删除%d条记录' % cur.rowcount)
