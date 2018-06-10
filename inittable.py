#!/usr/bin/env python
# encoding: utf-8


"""
@version: python27
@author: fafa
@site: http://www.phpgao.com
@software: PyCharm Community Edition
@file: InitTab.py
@time: 2017/2/27 0027 下午 10:33
"""
from mysql_db import MysqlDb


def init_db():
    sql_script = ''' create table contact(id integer primary key autoincrement not null,
    name varchar(20) not null,home_tel varchar(12),mobil_phone varchar(20),memo text);
    create table mygroup(id integer primary key autoincrement not null,
    name varchar(20) not null,memo text);
    create table table con_group(cid integer not null ,gid integer not null,
    foreign key(cid) preferences contact(id),foreign key(gid) preferences mygoup(id));
    '''
    with MysqlDb() as db:
        db.executescript(sql_script)


if __name__ == "__main__":
    init_db()
