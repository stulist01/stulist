#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

from dbconn import db_cursor

def create_db():
    sqlstr = """
    DROP TABLE IF EXISTS course;
    
    CREATE TABLE IF NOT EXISTS course  
    (
        cou_sn   INTEGER,     --序号
        cou_no   TEXT,        --学号
        name     TEXT,        --姓名
        birth  TEXT,        --出生日期
	    gender   TEXT,        --性别
		 class0   TEXT,        --班级
        PRIMARY KEY(cou_sn)
    );
    -- CREATE UNIQUE INDEX idx_course_no ON course(cou_no);

    CREATE SEQUENCE seq_cou_sn 
        START 10000 INCREMENT 1 OWNED BY course.cou_sn;   

    """
    with db_cursor() as cur :
        cur.execute(sqlstr) # 执行SQL语句
    
def init_data():
    sqlstr = """
    DELETE FROM course;

    INSERT INTO course (cou_sn, cou_no, name,birth,gender,class0)  VALUES 
        (1310650101, '1310650101', '齐琪','19950511', '男', '信息1301'), 
        (1310650102, '1310650102',  '柳风', '19950511', '男', '信息1301');
      

    """
    with db_cursor() as cur :
        cur.execute(sqlstr)    

if __name__ == '__main__':
    create_db()
    init_data()
    print('数据库已初始化完毕！')