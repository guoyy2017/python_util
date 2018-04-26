#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:18/4/18.下午2:16
'''

'''
https://www.cnblogs.com/wang1122/p/6709286.html
Python任务调度模块 – APScheduler
APScheduler是一个Python定时任务框架
在APScheduler中有四个组件：
触发器(trigger)包含调度逻辑，每一个作业有它自己的触发器，用于决定接下来哪一个作业会运行。除了他们自己初始配置意外，触发器完全是无状态的。
作业存储(job store)存储被调度的作业，默认的作业存储是简单地把作业保存在内存中，其他的作业存储是将作业保存在数据库中。一个作业的数据讲在保存在持久化作业存储时被序列化，并在加载时被反序列化。调度器不能分享同一个作业存储。
执行器(executor)处理作业的运行，他们通常通过在作业中提交制定的可调用对象到一个线程或者进城池来进行。当作业完成时，执行器将会通知调度器。
调度器(scheduler)是其他的组成部分。你通常在应用只有一个调度器，应用的开发者通常不会直接处理作业存储、调度器和触发器，相反，调度器提供了处理这些的合适的接口。配置作业存储和执行器可以在调度器中完成，例如添加、修改和移除作业。
你需要选择合适的调度器，这取决于你的应用环境和你使用APScheduler的目的。通常最常用的两个：
– BlockingScheduler: 当调度器是你应用中唯一要运行的东西时使用。
– BackgroundScheduler: 当你不运行任何其他框架时使用，并希望调度器在你应用的后台执行。
pip install apscheduler

trigger date, interval或者cron

cron定时调度
year (int|str) – 4-digit year
month (int|str) – month (1-12)
day (int|str) – day of the (1-31)
week (int|str) – ISO week (1-53)
day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
hour (int|str) – hour (0-23)
minute (int|str) – minute (0-59)
second (int|str) – second (0-59)
start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
end_date (datetime|str) – latest possible date/time to trigger on (inclusive)
timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)
和Linux的Crontab一样，它的值格式为：

Expression	Field	Description
*	any	Fire on every value
*/a	any	Fire every a values, starting from the minimum
a-b	any	Fire on any value within the a-b range (a must be smaller than b)
a-b/c	any	Fire every c values within the a-b range
xth y	day	Fire on the x -th occurrence of weekday y within the month
last x	day	Fire on the last occurrence of weekday x within the month
last	day	Fire on the last day within the month
x,y,z	any	Fire on any matching expression; can combine any number of any of the above expressions

interval 间隔调度
它的参数如下：
weeks (int) – number of weeks to wait
days (int) – number of days to wait
hours (int) – number of hours to wait
minutes (int) – number of minutes to wait
seconds (int) – number of seconds to wait
start_date (datetime|str) – starting point for the interval calculation
end_date (datetime|str) – latest possible date/time to trigger on
timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations

date 定时调度
最基本的一种调度，作业只会执行一次。它的参数如下：
run_date (datetime|str) – the date/time to run the job at
timezone (datetime.tzinfo|str) – time zone for run_date if it doesn’t have one already




APScheduler组成组件
Triggers

触发器,有自己的任务调度逻辑，每一个job单位都有触发器决定下一次何时运行。除了初始化的配置，他没有状态。

Job stores

储存调度任务，默认job对象，是储存在内存中，也可以用其他job对象把他们储存在各种数据库中；job保存到持久化仓库时，job数据要进行序列化，当加载job时也要进行反序列化。Job不能共享调度器。

Executors

是job运行的处理器，通常通过提交指定调用的job到进程或者线程池处理；当job完成后，通知发出一个适当的事件调度程序。

Schedulers

通常一个应用只有一个调度器，schdeuler开发者不直接处理jobs stores、Executors、Triggers, 相反，调度程序提供适当的接口来处理这些；配置job stores和executors通过调度器来完成，如增加，删除和修改。

APScheduler常用调度器
BlockingScheduler: 当应用程序中只有调度器时使用。

BackgroundScheduler: 不使用任何以下框架（asyncio、gevent、Tornado、Twisted、Qt），并且需要在你的应用程序后台运行调度程序

AsyncIOScheduler: 应用程序使用asyncio模块时使用

GeventScheduler: 应用程序使用gevent模块时使用

TornadoScheduler: Tornado应用程序时使用

TwistedScheduler: Twisted应用程序使用

QtScheduler: Qt应用程序时使用

APScheduler触发器
DateTrigger——日期触发器

添加此类触发器job之后，只运行一次，可以指定运行时间；若不指定则默认为当前时间。

正常使用时，使用add_job，不指定trigger类型，默认就是DateTrigger

指定trigger类型，可以使用字符串date，或者直接使用类DateTrigger的实例

# 示例代码
    from apscheduler.triggers.date import DateTrigger
    # 使用字符串方式1
    scheduler.add_job(date_tick)
    # 使用字符串方式2
    scheduler.add_job(date_tick, 'date')
    # 使用DateTrigger指定时间运行： 
    date = DateTrigger(datetime.now()+dt.timedelta(seconds=120))   
    scheduler.add_job(date_tick, date)
1
2
3
4
5
6
7
8
9
IntervalTrigger——间隔触发器

此触发器，可以指定开始时间start_date，结束时间end_date，以及间隔时间，

间隔时间可以有weeks/days/hours/minutes/seconds组成，

开始时间之后，每隔多少interval执行一次任务，直至结束时间，如果不指定结束时间，则一直执行

指定此类触发器类型，可以使用字符串interval，也可以使用类IntervalTrigger的实例对象

# 示例代码
    from apscheduler.triggers.interval import IngervalTrigger
    # 使用字符串方式
    scheduler.add_job(interval_tick,'interval',seconds=4,minutes=2,
                     start_date=datetime.now()+dt.timedelta(seconds=120),
                     end_date=datetime.now()+dt.timedelta(seconds=360))
    # 使用IntervalTrigger指定时间运行
    trigger = IntervalTrigger(seconds=60, 
                              start_date=datetime.now()+dt.timedelta(seconds=60),
                              end_date=datetime.now() + dt.timedelta(seconds=120))
    scheduler.add_job(date_tick, trigger)
1
2
3
4
5
6
7
8
9
10
11
CronTrigger——Cron触发器

类Unix系统中的Cron中，可以任意配置指定，年月日时分秒，周，每周几定时处理任务

由表达式（Expression）和字段（Field）组成，可以根据每个字段的表达式获取执行值，由调度器获取具体的执行日期

year’: ‘‘, ‘month’: 1, ‘day’: 1, ‘week’: ‘‘, ‘day_of_week’: ‘*’, ‘hour’: 0, ‘minute’: 0, ‘second’: 0

指定具体值，或者每分钟，或者每几分钟，或者每周几等当时
    year (int|str) – 4-digit year
    month (int|str) – month (1-12)
    day (int|str) – day of the (1-31)
    week (int|str) – ISO week (1-53)
    day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
    hour (int|str) – hour (0-23)
    minute (int|str) – minute (0-59)
    second (int|str) – second (0-59)
    start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
    end_date (datetime|str) – latest possible date/time to trigger on (inclusive)
    timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)
1
2
3
4
5
6
7
8
9
10
11
12
Expression	Field	Description
*	any	Fire on every value
*/a	any	Fire every a values, starting from the minimum
a-b	any	Fire on any value within the a-b range (a must be smaller than b)
a-b/c	any	Fire every c values within the a-b range
xth y	day	Fire on the x-th occurrence of weekday y within the month
last x	day	Fire on the last occurrence of weekday x within the month
last	day	Fire on the last day within the month
x,y,z	any	Fire on any matching expression; can combine any number of any of the above expressions




装饰器

from apscheduler.scheduler import Scheduler   
   
schedudler = Scheduler(daemonic = False)   
  
@schedudler.cron_schedule(second='*', day_of_week='0-4', hour='9-12,13-15')   
def quote_send_sh_job():   
    print 'a simple cron job start at', datetime.datetime.now()   
   
schedudler.start()  



DEMO
from pymongo import MongoClient
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


def my_job():
    print 'hello world'
host = '127.0.0.1'
port = 27017
client = MongoClient(host, port)

jobstores = {
    'mongo': MongoDBJobStore(collection='job', database='test', client=client),
    'default': MemoryJobStore()
}
executors = {
    'default': ThreadPoolExecutor(10),
    'processpool': ProcessPoolExecutor(3)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
scheduler.add_job(my_job, 'interval', seconds=5)

try:
    scheduler.start()
except SystemExit:
    client.close()
'''





if __name__ == '__main__':
    pass