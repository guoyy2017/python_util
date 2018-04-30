#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/4/26.下午1:52
'''

'''
MONGO 用法

pip install pymongo

安装依赖
pip install pymongo[gssapi,srv,tls]

PyMongo 是 MongoDB 的 Python 接口开发包。
创建Connection时，指定host及port参数
>>> import pymongo
>>> conn = pymongo.Connection(host='127.0.0.1',port=27017)

连接数据库
>>> db = conn.ChatRoom
或
>>> db = conn['ChatRoom']

连接聚集
>>> account = db.Account
或
>>> account = db["Account"]

查看全部聚集名称
>>> db.collection_names()

查看聚集的一条记录
>>> db.Account.find_one()
>>> db.Account.find_one({"UserName":"keyword"})

查看聚集的字段
>>> db.Account.find_one({},{"UserName":1,"Email":1})
{u'UserName': u'libing', u'_id': ObjectId('4ded95c3b7780a774a099b7c'), u'Email': u'libing@35.cn'}
>>> db.Account.find_one({},{"UserName":1,"Email":1,"_id":0})
{u'UserName': u'libing', u'Email': u'libing@35.cn'}

查看聚集的多条记录
>>> for item in db.Account.find():
        item
>>> for item in db.Account.find({"UserName":"libing"}):
        item["UserName"]

查看聚集的记录统计
>>> db.Account.find().count()
>>> db.Account.find({"UserName":"keyword"}).count()

聚集查询结果排序
>>> db.Account.find().sort("UserName")  --默认为升序
>>> db.Account.find().sort("UserName",pymongo.ASCENDING)   --升序
>>> db.Account.find().sort("UserName",pymongo.DESCENDING)  --降序

聚集查询结果多列排序
>>> db.Account.find().sort([("UserName",pymongo.ASCENDING),("Email",pymongo.DESCENDING)])


添加记录
>>> db.Account.insert({"AccountID":21,"UserName":"libing"})

修改记录
>>> db.Account.update({"UserName":"libing"},{"$set":{"Email":"libing@126.com","Password":"123"}})

删除记录
>>> db.Account.remove()   -- 全部删除
>>> db.Test.remove({"UserName":"keyword"})
'''

if __name__ == '__main__':
    pass