# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/22 0022 上午 11:27
@Author  : fengaijun
@File    : parseini.py

'''
import configparser

config= configparser.ConfigParser()
config.read("config.ini",encoding="utf-8")
# #获取ini文件所有节点
nodes = config.sections()
print(nodes)
# #获取指定节点下的所有信息项
# elements = config.options(section="database")
# print("数据库信息:",elements)
# #获取指定节点下的所有信息项信息值
# value = config.get(section="accountinfo",option="username")
# print("账号姓名:",value)

# 获取某个节点下的所有选项及选项值 ‐‐‐》元组列表
ele_values = config.items(section="accountinfo")
print(ele_values)
def getElementvalue(section,option):
    return config.get(section=section,option=option)
#p判断节点存在性，决定是否写入节点
# sectionname="redis"
# if sectionname not in nodes:
#     config.add_section(sectionname)
#
# config.set(section=sectionname,option="username",value="admin")
# config.set(section=sectionname,option="password",value="123456")
# with open("config.ini","w+",encoding="utf-8") as file:
#     print("开始写入。。。。。")
#     config.write(file)
'''
覆盖添加信息项
'''
def addElementValue(sectionname,ele_values):
    if sectionname not in nodes:
        config.add_section(sectionname)
    for x in ele_values:
        config.set(section=sectionname, option=x[0], value=x[1])
    with open("config.ini", "w+", encoding="utf-8") as file:
         print("开始写入。。。。。")
         config.write(file)
         print("写入完成。。。。")
'''
追加添加信息项
'''
def addElementValue1(sectionname,optionname,value):
    # if sectionname not in nodes:
    #     config.add_section(sectionname)
    config.set(section=sectionname, option=optionname, value=value)
    with open("config.ini", "w+", encoding="utf-8") as file:
         print("开始写入。。。。。")
         config.write(file)
         print("写入完成。。。。")
#修改信息项元素值
def updateElementValue(sectionname,optionname,value):
    if sectionname not in nodes:
       print("该节点不存在！！！")
    elif optionname not in config.options(section=sectionname):
        print("该信息项不存在！！！")
    else:
        config.set(section=sectionname,option=optionname,value=value)
        with open("config.ini", "w+", encoding="utf-8") as file:
            print("开始写入。。。。。")
            config.write(file)
            print("写入完成。。。。")
#删除节点[节点所属的信息项也同步删除]
def deleteNode(sectionname):
    if sectionname not in config.sections():
        print(f"{sectionname}节点不存在！！！")
    else:
        config.remove_section(section=sectionname)
        with open("config.ini","w+",encoding="utf-8") as file:
            print("开始删除。。。。")
            config.write(file)
            print("删除完成。。。。")
#删除节点所属信息项
def deleteElement(sectionname,optionname):
    if sectionname not in config.sections():
        print(f"{sectionname}节点不存在！！！")
    elif optionname not in config.options(section=sectionname):
        print(f"{optionname}信息项不存在！！！")
    else:
        config.remove_option(section=sectionname,option=optionname)
        with open("config.ini","w+",encoding="utf-8") as file:
            print("开始删除信息项！！！")
            config.write(file)
            print("信息项删除成功！！！")
if __name__ == '__main__':
    # addElementValue("serverinfo",ele_values)
    # updateElementValue("App","username1","陈近南")
    #  deleteNode("App")
    # deleteElement("serverinfo","ip")
     addElementValue1("serverinfo","ip","10.145.6.12")