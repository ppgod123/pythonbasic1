# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/28 0028 下午 8:35
@Author  : fengaijun
@File    : Decorators.py

'''
import time

def runTime(func):
    def wraper():
        start = time.time()
        func()
        end = time.time()
        cost = end -start
        print(f"总计耗时:{cost}")
    return wraper
@runTime
def welcome():
    print("欢迎来到数字浙江！！！")
    time.sleep(1)

#非装饰器调用函数
# a= runTime(welcome)
# a()

#装饰器调用函数
welcome()