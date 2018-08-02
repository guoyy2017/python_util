#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/14.下午4:30
pip install py-leveldb
def initialize():
    db = leveldb.LevelDB("students");
    return db;

def insert(db, sid, name):
    db.Put(str(sid), name);

def delete(db, sid):
    db.Delete(str(sid));

def update(db, sid, name):
    db.Put(str(sid), name);

def search(db, sid):
    name = db.Get(str(sid));
    return name;

def display(db):
    for key, value in db.RangeIter():
        print (key, value);
2.7字符串操作需要u''
'''

from leveldb import LevelDB

db = LevelDB('./data')
db.Put(str(u'nihao'),'wobuxing')
print db.Get(str(u'nihao'))