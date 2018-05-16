#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/16.上午10:52
'''

from celery.schedules import crontab

# 说明: 导入其它模块

# BROKER_URL = 'amqp://root:qwertyuiop@172.24.10.1:5672//'

# CELERY_RESULT_BACKEND = 'redis://172.24.10.1:6379/0'

BROKER_URL = 'amqp://root:qwertyuiop@10.2.5.51:5672//'

CELERY_RESULT_BACKEND = 'redis://10.2.5.51:5123/0'

CELERY_TASK_SERIALIZER = 'msgpack'

CELERY_RESULT_SERIALIZER = 'json'

CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24

CELERY_ACCEPT_CONTENT = ['json', 'msgpack']

CELERYD_MAX_TASKS_PER_CHILD = 40

#timedelta和crontab来定义计划任务,crontab的精度无法精确到秒时可使用timedelta代替
CELERYBEAT_SCHEDULE = {

    'send_mail': {

        'task': 'work.notify.email.send_mail',

        # 'schedule': timedelta(minute=1),

        'schedule': crontab(minute='*/1'),

        'args': ('usr', 'sub', 'msg')

    }

}

if __name__ == '__main__':
    pass