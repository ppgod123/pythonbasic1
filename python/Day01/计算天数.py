# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/16 0016 下午 5:26
@Author  : fengaijun
@File    : 计算天数.py

'''

import time

#获取当前时间-时间戳
time1 = time.time()
#时间戳转元祖
tupletime = time.localtime(time1)

#获取1949年10月1号-到当前日期，总天数
days=0
year1=1949
year2= tupletime.tm_year
curr_mon = tupletime.tm_mon
curr_mon_day = tupletime.tm_mday
print(curr_mon_day)
M0=[10,11,12]
M1=[1,2,3]

#判断是否闰年
def isleapyear(days,year1,year2):
    for Y in range(year1+1,year2):
           if((Y%4==0 and Y%100!=0) or Y%400==0):
               days+=366
               print(f"当前年份{Y}，闰年，累计天数{days}")
           else:
               days+=365
               print(f"当前年份{Y}，平年，累计天数{days}")
    return days
#判断不同月份天数
def moncountdays(days,M0,year):
    for M in M0:
        if M in [1, 3, 5, 7, 8, 10, 12] and M!=curr_mon:
            days += 31
        elif M in [4, 6, 9, 11] and M!=curr_mon:
            days += 30
        elif M==curr_mon:
            days+=curr_mon_day
        elif M == 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and M!=curr_mon:
            days += 29
        else:
            days += 28
    return days



days = moncountdays(days,M0,year1)
print("49年当年总天数",days)
days = isleapyear(days,year1,year2)
print("49年10月1日至2022年总天数",days)
days = moncountdays(days,M1,year2)
print("49年10月1日至今天总天数:",days)

# aa=moncountdays(0,M1,year2)
# print(aa)