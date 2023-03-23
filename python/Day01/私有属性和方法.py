# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/20 0020 下午 5:02
@Author  : fengaijun
@File    : 私有属性和方法.py

'''

class student():
    #私有属性
    __weight = 190
    __height = 160
    sex = "张三"

    #私有方法
    def __speak(self):
        print("这是一个私有方法！！！")
        return "这是一个私有方法22！！！"

    def speak(self):
        print("我说的就是中文！！！")
        #内部获取私有属性
        print(f"告诉你一个秘密，我的身高{self.__height},我的体重{self.__weight}")
        #内部调用私有方法
        self.__speak()

dd=student()
dd.speak()
print(dd.sex)
# dd.__speak()   无法直接获取
# print(dd.__weight,dd.__height)

#实例化对象获取私有属性
print("实例化对象获取私有属性",dd._student__weight,dd._student__height)
#实例化对象获取私有方法
print("实例化对象获取私有方法",dd._student__speak())
dd._student__speak()


