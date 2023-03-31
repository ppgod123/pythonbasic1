# -*- coding: utf-8 -*- 
'''
@Time : 2023/3/30 18:35 
@Author : 冯爱军 
@File : fansetest1.py
'''
class Student:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("吃饭！！！")
    def sleep(self):
        print("睡觉！！！")
    def playGame(self):
        print("玩游戏！！！")
actionList = ["eat","sleep","playGame"]
num = int(input("请输入您的选择:"))
if num>3 or num<1:
    print("请输入1-3范围内整数！！！")
elif not isinstance(num,int):
    print("请输入1-3范围内整数！！！")
else:
    # print("执行啦！！！")
    # print(actionList[num-1])
    andy = Student("andy")
    getattr(andy,actionList[num-1])()
    setattr(andy,'name',"Faker")
    print(getattr(andy,'name'))
    print(hasattr(andy,'name'))
    print(hasattr(andy,'age'))
    delattr(andy,'name')
    print(hasattr(andy,'name'))
#外部函数映射到类内部函数
def walk():
    print("我在走路！！！！")

setattr(andy,'eat',walk)
getattr(andy,'eat')()
andy.eat()
