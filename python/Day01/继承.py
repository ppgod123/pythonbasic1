# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/21 0021 下午 3:04
@Author  : fengaijun
@File    : 继承.py

'''

class father01():
    name = "王德发"
    __haha = "haha"
    def speak(self):
        print("说话！！！")
    def eat(self):
        print("吃饭！！！")
    def __heihei(self):
        print("嘿嘿！！！")
    def swim(self):
        print("孙杨,游泳啦！！！")
class father02():
    name = "王德发02"
    __haha = "haha"
    def speak(self):
        print("吹牛！！！")
    def eat(self):
        print("恰饭啦！！！")
    def __heihei(self):
        print("嘿嘿嘿！！！")
class father03():
    name = "王德发03"
    __haha = "haha"
    def speak(self):
        print("放屁！！！")
    def eat(self):
        print("用膳！！！")
    def __heihei(self):
        print("嘿嘿啦！！！")
    def walk(self):
        print("跑步啦！！！")
    def swim(self):
        print("游泳啦")
#继承
class son(father01):
    #对父类speak方法重载
    def speak(self):
        print("演讲！！！")
#多继承  按就近原则（从左到右）-取父类的属性、调用相关方法
class son1(father02,father01,father03):
    def gg(self):
        print("gg啦！！！")

son_test1 = son()

son_test1.speak()
son_test1.eat()
#私有属性、方法只能类内部调用
# son1.__heihei()
print(son_test1.name)
# son1.__haha

#多继承
son2 = son1()
print(son2.name)
son2.speak()
son2.eat()
son2.gg()
son2.swim()
super(son,son_test1).speak()   #用子类对象调用父类已被覆盖的方法