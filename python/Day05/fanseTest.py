# -*- coding: utf-8 -*- 
'''
@Time : 2023/3/30 18:15 
@Author : 冯爱军 
@File : fanseTest.py
'''


class MyClass:
    def __init__(self, value):
        self.value = value

    def say_hello(self):
        print("Hello, world!")


my_object = MyClass(42)

# 使用getattr获取对象的属性和方法
print(getattr(my_object, 'value'))  # 输出: 42
getattr(my_object, 'say_hello')()  # 输出: Hello, world!

# 使用setattr设置对象的属性和方法
setattr(my_object, 'value', 99)
print(getattr(my_object, 'value'))
my_object.say_hello = lambda: print("Hi, there!")
my_object.say_hello()  # 输出: Hi, there!

# 使用delattr删除对象的属性和方法
delattr(my_object, 'value')
delattr(my_object, 'say_hello')
