# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/22 0022 下午 3:00
@Author  : fengaijun
@File    : test.py

'''
from python.Day02.parseini import getElementvalue
from python.Day01.pupil import creatpupil
from python.Day01.计算天数 import isleapyear

value = getElementvalue("database","port")
print(value)

aa = creatpupil("andy",50)
aa.walk()
aa.walk()
print(aa.weight)

days = isleapyear(0,2000,2023)
print(days)
print(lambda num1=1,num2=2,num3=3:num1+num2+num3)