# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/20 0020 下午 3:34
@Author  : fengaijun
@File    : 类实例化.py

'''

class Testclass():
    #学生数量
    num=0

    def __init__(self):
        Testclass.addnum()
    @classmethod
    def addnum(cls):
        cls.num+=1
    @classmethod
    def getnum(cls):
        return cls.num

class Student(Testclass):
    pass

aa=Student()
bb=Student()
cc=Student()
print(Testclass.getnum())