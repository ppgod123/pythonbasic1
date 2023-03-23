# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/17 0017 上午 10:34
@Author  : fengaijun
@File    : 异常模块.py

'''

# x=3
# if x>5:
#     raise Exception(f'x不能大于5，x的值为:{x}')
# elif x>5&x<10:
#     raise Exception("x不能小于10，x的值:".format(x))



def add(a:int,b:int):
    return a+b


print(add(2,3))
# print(add('12',12))
a=0
b=0
try:
    a = eval(input("请输入第一个数字:"))
    b = input("请输入第二个数字:")
    print(add(a,b))
except:
    raise Exception(f"输入值存在非整数,a的值{a},a的数据类型{type(a)};b的值{b},b的数据类型{type(b)}")
