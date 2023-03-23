# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/14 0014 上午 11:18
@Author  : fengaijun
@File    : List数据类型.py

'''

list=[1,2,3,4,5,(1,2,3),[1,2,3]]
print(list)
print(type(list))
#获取列表最后一个元素
print(list[-1])
#获取前四个元素
print(list[:4])
#步长为2提取元素
print(list[::2])
#删除元素
del list[0]
print(list)
#列表运算符+
list = list + ["韦小宝","陈近南"]
print(list)
#列表运算符*
print(list*3)
#列表运算符in
print("韦小宝" in list)
#列表计算符 not in
print("陈近南" not in list)

#列表内置函数-追加append
list2 = [1,2,3,5,4]

list2.append(33333)
print(list2)
list2.insert(0,"哈哈哈")
list2.insert(-1,"我爱一条柴")
print(list2)
list2.extend([(1,2,3),[1,99,3],3434,"康熙","雍正"])
print(list2)

#根据索引删除元素
list2.pop(1)
print(list2)
#根据值删除对应元素
list2.remove("康熙")
print(list2)

#清空列表
list.clear()
print(list)

#查找返回值的索引值，不存在则报异常
aa = list2.index(33333)
print(aa)

#排序
list3 = [33,2,12,3,5,99,111,2334,5]
list3.sort()
print(list3)
#列表反转
list2.reverse()
print(list2)

#统计个数
print(list2.count(33333))
