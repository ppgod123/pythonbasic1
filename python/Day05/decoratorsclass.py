# -*- coding: utf-8 -*- 
'''
@Time : 2023/3/31 11:16 
@Author : 冯爱军 
@File : decoratorsclass.py
'''
import time

# 定义装饰类‐‐‐‐‐》本质类 作用：原来功能+扩展功能
class A:
 #原来功能 self._func()
 def __init__(self,func):
   self._func=func

#扩展功能
 def __call__(self,*args,**kwargs):
   start = time.time()
   # 原来功能
   self._func() # 原来功能
   end = time.time()
   cost = end - start
   print(f"统计函数总共耗时{cost}秒1")


@A
def welcome_vip():
  """被装饰器函数"""
  print("欢迎来到码尚学院VIP课堂")

welcome_vip()