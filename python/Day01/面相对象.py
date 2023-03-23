# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/20 0020 上午 11:04
@Author  : fengaijun
@File    : 面相对象.py

'''

class people():
    height = 188
    weight ="我爱一条柴"
    def speak(self):
        print("我说的就是中国话！！！")

    # 对象和类均可调用的公共方法
    @staticmethod
    def static_method():
        print("这是一个静态方法！！！！")
    @classmethod
    def class_method(cls):
        print(cls,type(cls))
        print("这是一个类方法！！！")
    # def __init__(self):
    #     print("创建了一个无参构造函数！！！")
    def __init__(self,name,age):
        print(f"带参构造函数创建对象{name},{age}")
    def __getattribute__(self, item):
        print("获取类/对象属性")
    def __str__(self):
        print("替换后的默认输出")

    def __del__(self):
        print("调用del方法，释放对象的内存地址")

# hanxin = people()
liubang = people("张三",22)
print(liubang)

# print(people.__dict__)
# print(people.__doc__)
# print(people.__name__)
# print(people.__module__)



liubang.class_method()
people.class_method()
print("---------------------------")