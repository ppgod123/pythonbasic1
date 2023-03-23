# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/15 0015 下午 4:53
@Author  : fengaijun
@File    : 文件操作.py

'''
import os
import shutil
import random
import stat
str01 ="""python基础
python接口自动化
pythonWeb自动化
pythonApp自动化
"""

# file = open("aa.txt","w+",encoding="utf-8")
# file.write(str01)
# file.close()
#创建文件
# with open("aa1.txt","w+",encoding="utf-8") as file:
#     #一旦有异常，自动关闭文件对象
#     file.writelines(str01)
# #读取文件
# with open("aa1.txt","r",encoding="utf-8") as file2:
#     #初始指针
#     print(file2.tell())
#     #一旦有异常，自动关闭文件对象
#     #print(file2.read(10))
#     file2.seek(6,0)  #0-文件的开头作为移动字节的参考位置 1-当前位置作为移动字节的参考位置 2-将文件的末尾作为参考位置
#     print(file2.tell())
#     print(file2.readline())
#     print(file2.readlines())
#     #读取后指针
#     print(file2.tell())
# #文件内容追加
# with open("aa1.txt","a+",encoding="utf-8") as file3:
#      file3.write("Jekins持续集成")
#      print(file3.tell())
#      #file3.close()
#      file3.seek(0,0)
#      #print(file3.readline())
#      print(file3.readlines())

#删除文件
#os.remove("aa.txt")
# #创建目录
# os.mkdir(r"D:\PycharmProjects\pythonbasic\python\Day01\36")
#
# os.makedirs(r"D:\PycharmProjects\pythonbasic\python\Day01\3301\44\58")
# #删除目录(空目录)
# os.rmdir(r"D:\PycharmProjects\pythonbasic\python\Day01\34")
# #删除非空目录
# shutil.rmtree(r"D:\PycharmProjects\pythonbasic\python\Day01\3301\44\56")
# #文件夹重命名
# old =r"D:\PycharmProjects\pythonbasic\python\Day01\3301"
# new =r"D:\PycharmProjects\pythonbasic\python\Day01\3302"
# os.rename(old,new)

#获取当前目录路径
path1 = os.getcwd()
print(path1)
#当前目录下创建文件夹
aa12 = random.randint(1,10000)
print(aa12,type(aa12))
print('kk'+ str(aa12))
dirname01 = 'kk'+ str(aa12)
path2 = os.path.join(path1,dirname01)
print(path2)
os.mkdir(path2)
#获取目录或则文件的访问权限
isExist=os.access(path1,os.F_OK)
isRead=os.access(path1,os.R_OK)
isWrite=os.access(path1,os.W_OK)
print(isExist,isRead,isWrite)

#判断路径是否是文件夹
print(os.path.isdir(path2))
#判断路径是否是文件
print(os.path.isfile(path2))

#更改文件目录权限
#OTH其他用户  GRP用户组 USR拥有者 R可读 X可执行 W可写
os.chmod(path2, stat.S_IROTH)