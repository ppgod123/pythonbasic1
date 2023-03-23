# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/20 0020 下午 5:47
@Author  : fengaijun
@File    : pupil.py

'''

class pupil():

    def __init__(self,name ,weight):
        print("带参构造函数")
        self.name = name
        self.weight = weight
    def walk(self):
        self.weight-=0.5
        return self.weight
    def eat(self):
        self.weight+=1
        return self.weight
def creatpupil(name,weight):
    return pupil(name,weight)

# xiaoming = pupil("小明",75)
# xiaomei = pupil("小美",55)
# xiaoming.walk()
# print("小明的当前体重：",xiaoming.weight)
# xiaoming.walk()
# print("小明的当前体重：",xiaoming.weight)
# xiaoming.eat()
# print("小明的当前体重：",xiaoming.weight)