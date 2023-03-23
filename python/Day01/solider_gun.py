# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/21 0021 下午 4:04
@Author  : fengaijun
@File    : solider_gun.py

'''
gunlist1 = []
class solider():
    def __init__(self,name,gunlist):
        self.name =name
        self.gunlist = gunlist
    def __str__(self):
        info = []
        for x in self.gunlist:
           # print(x)
           # print(f"士兵的姓名:{self.name}" + str(x))
           info.append(f"士兵的姓名:{self.name};" + str(x))
        return str(info)
    def addgun(self,gunaa):
        self.gunlist.append(gunaa)
        # print("配枪数:",len(self.gunlist))
    def fire(self):
        print("开火了！！！")
        for x in self.gunlist:
          if x.bullets_num >0:
            x.bullets_num-=1
          else:
            print(f"{x.gun_name}子弹打光了！！!请装填")
    def reloading(self):
        print("弹药装填！！！")
        for x in self.gunlist:
          if x.bullets_num <30 and x.gun_name =="AK47":
            x.bullets_num+=1
          elif x.bullets_num <10 and x.gun_name =="马格南":
            x.bullets_num += 1
          elif x.bullets_num ==30 and x.gun_name =="AK47":
              print(f"{x.gun_name}弹匣子弹已装满！！！")
          else:
            print(f"{x.gun_name}弹匣子弹已装满！！！")

class gun():
    def __init__(self,gun_name,bullets_num):
        self.gun_name = gun_name
        self.bullets_num = bullets_num
    def __str__(self):
        return f"枪支名称:{self.gun_name},弹匣剩余子弹：{self.bullets_num}"

gun01 = gun("AK47",30)
gun02 = gun("马格南",10)
# print(gun01)
solider1 = solider("瑞恩",gunlist1)
solider1.addgun(gun01)
solider1.addgun(gun02)
for y in range(1,41):
    solider1.fire()
for z in range(1,33):
    solider1.reloading()
print(solider1)