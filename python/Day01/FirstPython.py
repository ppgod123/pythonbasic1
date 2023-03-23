# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/13 0013 上午 9:45
@Author  : fengaijun
@File    : SecondPython.py

'''
import keyword
import math
import random
print("Hello World!!!","Learning is an ongoing process!!!",end="");print("我爱一条柴")
#print(keyword.kwlist)
num_1=10
num_2=10
num_3=10
num_4=10
num_5=10
total = num_1+\
        num_2+\
        num_3+\
        num_4+\
        num_5
print(total**2)
print(total*2)
print(total+1)
print(total-1)
print(total/3)
print(total//3)
print(total%3)
print(math.floor(4.77))
print(math.ceil(4.12))
print(random.random())
print(random.randint(100,200))
print(round(4.7))
print(round(4.1))
print(math.trunc(8.52))
#字符串截取
str = "Learning is an ongoing process!!!"
#截取除第一个字符
print(str[0])
#截取2-5长度字符
print(str[1:5])
#截取末尾4位
print(str[-4:])
#倒序截取
print(str[::-1])
#隔一位截取
print(str[::2])
#字符串拼接
print(str+"韦小宝！！！")
#特殊字符串转义
print("123123\\n123123")
print("123123\"123123")
print('123123\'123123')
print("123123\\t123123")
print("123123\\123123")
print("123123\\000123123")
print('C:\\Users\\Administrator\\Desktop\\Java自动化')
print(R'C:\Users\Administrator\Desktop\Java自动化')
#字符串运算
#字符串拼接+
print(str+"韦小宝！！！")
#字符串拼接*
print(str * 5)
#字符串拼接in
print('韦小宝' in str)
#字符串拼接not in
print('康熙' not in str)
#字符串比较 is
s1="123"
s2="123"
print(s1 is s2)
print(s1 is not s2)
print(s1==s2)
print(s1!=s2)

#字符串格式化，方式一
print("%s[%s期,工龄：%d]欢迎学习Python！！！"%('冯爱军','M2301',5))

#字符串格式化，方式二
print("{}[{}期,工龄：{}]欢迎学习Python！！！".format('冯爱军','M2301',5))
print("{1}[{1}期,工龄：{1}]欢迎学习Python！！！".format('冯爱军','M2301',5))

#字符串格式化，方式三
name='冯爱军'
qs='M2303'
gl=5
print(f"{name}[{qs}期,工龄：{gl}]欢迎学习Python！！！")

#字符串内置函数

print('-'.join(qs))

print(qs.find('2'))

print(qs.count('1'))

print(qs.split('3'))

print(qs.replace('23','哈哈哈'))

print(qs.index('0'))