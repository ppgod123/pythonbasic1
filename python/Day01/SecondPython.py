# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/13 0013 上午 9:45
@Author  : fengaijun
@File    : SecondPython.py

'''

#元组

#创建空元组
tup1=()
print(tup1)
print(type(tup1))
#创建只包含一个元素的元组
tup2=(123,)
print(tup2)
print(type(tup2))
#元组分割
tup3=(1,2,3,4,5,6,77777,8,"ahahahahah","9999999999")
#取元组第一个值
print(tup3[0])
#取元组除后2位位值
print(tup3[:-2])
#step步数位2，取值
print(tup3[::2])
#倒序，取值
print(tup3[::-1])
#元组拼接+
print(tup2+tup3)
#删除元组
# del tup3
# print(tup3)

#元组计算符+、*、in、not in
print(tup3 * 3)

print(1 in tup3)
print(1 not in tup3)

