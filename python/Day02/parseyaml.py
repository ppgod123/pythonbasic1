# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/22 0022 下午 5:52
@Author  : fengaijun
@File    : parseyaml.py

'''
import yaml
import os
#yaml文件内容写入
modules=["中文","pytest","unittest","requests","requests"]
with open("modules.yaml","w+") as file:
 yaml.dump(data=modules,stream=file,allow_unicode=True,encoding="utf‐8")
#yaml文件读取
with open("modules.yaml","r") as file:
 data= yaml.load(stream=file, Loader=yaml.FullLoader)
 print(data)
def writeyaml(path,data):
    with open(path, "w+") as file:
        yaml.dump(data=data, stream=file, allow_unicode=True, encoding="utf‐8")

def readyaml(path1):
    with open(path1,"r") as file:
       data = yaml.load(stream=file,Loader=yaml.FullLoader)
       return data

if __name__ == '__main__':
   # data1 = readyaml("configyaml1.yaml")
   # print(data1)
   # print(data1[0]["account"]["username"])
   # print(os.getcwd())
   # 获取文件所在当前目录的绝对路径 ，等于os.getcwd()
   cur = os.path.dirname(os.path.abspath(__file__))
   #:获取当前文件上一层目录的绝对路径
   per = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
   print(per)
   file_path = os.path.join(per, 'Day01\configyaml1.yaml')
   # D:\PycharmProjects\pythonbasic\python\Day01\aa1.txt
   # file_path = os.path.abspath()
   data2 = readyaml(file_path)
   print(data2)
   print(data2[1]["database"]["ip"])