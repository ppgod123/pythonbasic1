# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/14 0014 下午 2:09
@Author  : fengaijun
@File    : dict数据类型.py

'''
dict = {"姓名":"Andy","年龄":30,"性别":"男","职位":"开发工程师"}
print(dict)
print(type(dict))
#通过Key取值
print(dict["姓名"])
print(dict.get("姓名"))
#通过Key修改元素值
dict["姓名"] = "黄飞鸿"
print(dict)
#删除元素
del dict["姓名"]
print(dict)

#复制字典
dict1 = dict.copy()
dict.clear()
print(dict1)
print(dict)

#创建一个字典，key确定，值不确定，暂定为null
keys= ["姓名","年龄","身高","体重","学历","性别"]

dict3=dict.fromkeys(keys, "null")
print(dict3)
print(type(dict3))

#循环读取字典中所有数据key value
for x,y in dict1.items():
    print(x,y)

#字典合并
add = {"xz":500000}
dict1.update(add)
print(dict1)

dict1.update(dict3)
print(dict1)

#删除元素-根据key进行删除
dict1.pop("年龄")
print(dict1)
#默认删除最后一个元素,若字典为空则报异常
dict1.popitem()
print(dict1)

