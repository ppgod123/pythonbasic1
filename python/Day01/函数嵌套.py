# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/15 0015 下午 2:52
@Author  : fengaijun
@File    : 函数嵌套.py

'''
#调用嵌套
def A():
    print("我爱一条柴")
def B():
    print("含笑半步癫")
    A()

B()

#定义嵌套
def C():
    print("哈沙给")
    def D():
        print("人生能有机会哦不！！！")
    D()
C()

#匿名函数
sum = lambda num1,num2,num3:num1+num2+num3
print(sum(1,4,56))

#递归调用  1-100求和
sum = 0
def E(n):
    if n>0:
        return n+E(n-1)
    else:
        return 0

sum = E(100)
print(sum)
