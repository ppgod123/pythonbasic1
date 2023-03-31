# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/28 0028 下午 8:35
@Author  : fengaijun
@File    : Decorators.py

'''
import time

def runTime(func):
    def wraper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        cost = end -start
        print(f"总计耗时:{cost}")
    return wraper
@runTime
def welcome():
    print("欢迎来到数字浙江！！！")
    time.sleep(1)
@runTime
def SUM(x,y):
    sum = 0
    sum = x+y
    time.sleep(1)
    print(f"两数之和:{sum}")
#非装饰器调用函数
# a= runTime(welcome)
# a()

#装饰器调用函数
# welcome()
SUM(1,2)
