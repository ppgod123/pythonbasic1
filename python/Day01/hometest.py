# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/21 0021 上午 9:44
@Author  : fengaijun
@File    : hometest.py

'''
furniture_names =[]
#初始化家具列表为空
class home():
    def __init__(self,home_type,total_area,residual_area,furnitures):
        self.home_type = home_type
        self.total_area = total_area
        self.residual_area = residual_area
        self.furnitures = furnitures
    def __str__(self):
        return f"户型：{self.home_type},总面积:{self.total_area},剩余面积:{self.residual_area},家具名称:{furniture_names}"
    def addfurniture1(self,home,furniture):
        home.furnitures.insert(-1, furniture)
        home.residual_area-=furniture.floor_space
        return home.residual_area
    def addfurniture(self,furniture):
        self.furnitures.insert(-1, furniture)
        self.residual_area-=furniture.floor_space
        return self.residual_area
class furniture():
    def __init__(self,furniture_name,floor_space):
        self.furniture_name = furniture_name
        self.floor_space = floor_space


home1 = home("三室一厅",111.5,111.5,furnitures = [])
print(home1)
bed = furniture("床",4)
wardrobe = furniture("衣柜",2)
table = furniture("餐桌",1.5)
home1.addfurniture(bed)
home1.addfurniture(wardrobe)
home1.addfurniture(table)


for furniture in home1.furnitures:
    furniture_names.insert(-1,furniture.furniture_name)
print(furniture_names)

print("户型："+home1.home_type,"总面积:"+str(home1.total_area),"剩余面积:"+str(home1.residual_area),"家具名称:"+str(furniture_names))
print(home1)