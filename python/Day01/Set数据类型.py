# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/14 0014 下午 2:47
@Author  : fengaijun
@File    : Set数据类型.py

'''

Set1 = {1,2,3,4,5,6,(1,2,3,4),"123123"}
print(Set1)
print(type(Set1))

#创建空集合
set2 = set()
print(type(set2))
print(set2)

#运算-交集
A={1,2,3,4,5,5}
B={3,4,5,6,7,8,9,9}

print(A&B)
print("交集",A.intersection(B))
#运算-并集
print(A|B)
print("并集",A.union(B))
#y运算-差集
print(A-B)
print("差集",A.difference(B))
#运算-异或
print(A^B)
print("异或",A.symmetric_difference(B))

print(list(A)[2])