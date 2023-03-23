# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/16 0016 下午 4:21
@Author  : fengaijun
@File    : time模块.py

'''

import time
import datetime
import calendar

#获取当前时间-时间戳
time1 = time.time()
print(time1)
#获取现在时间元组
print(time.localtime())

#时间戳转元祖
tupletime = time.localtime(time1)
print(tupletime)
print(tupletime.tm_year,tupletime.tm_mon,tupletime.tm_yday,tupletime.tm_mday,tupletime.tm_wday,tupletime.tm_hour,tupletime.tm_min,tupletime.tm_sec)
print(type(tupletime.tm_yday))
#元组转时间戳
time2 = time.mktime(tupletime)
print(time2)

#时间元组---》字符串格式化
timestr=time.strftime("%Y/%m/%d  %H:%M:%S",tupletime)
print(timestr,type(timestr))

#字符串转时间元组
tulpletime2= time.strptime(timestr,"%Y/%m/%d  %H:%M:%S")
print(tulpletime2)

#获取当天时间
dt = datetime.datetime.today()
print(dt)
dt = datetime.datetime.now()
print(dt)
#将datetime转换成时间戳
dt = datetime.datetime.now().timestamp()
print(dt)
#将时间戳转换成datetime
aa =datetime.datetime.fromtimestamp(dt)
print(aa)
#将datetime转换成字符串
cc = aa.strftime("%Y/%m/%d %H:%M:%S")
print(cc)
#将字符串转换成datetime
bb = datetime.datetime.strptime(cc,"%Y/%m/%d %H:%M:%S")
print(bb)

#将周日设置为第一天
calendar.setfirstweekday(6)
print(calendar.firstweekday)
#判断指定年份是否是闰年
print(calendar.isleap(2000),calendar.isleap(2023))
#返回年份区间的闰年数量
print(calendar.leapdays(2021,2023))
print(calendar.leapdays(2000,2023))

# weekday(year, month, day)：获取指定日期为星期几 0-周一 1-周二 2-周三 3-周四 4-周五 5-周六 6-周日
print(calendar.weekday(2023,3,14))  #2
#返回包含星期的英文缩写，n表示英文缩写所占的宽度
print(calendar.weekheader(3))

