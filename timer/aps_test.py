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
'''





if __name__ == '__main__':
    pass