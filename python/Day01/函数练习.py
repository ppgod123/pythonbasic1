# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/15 0015 上午 11:00
@Author  : fengaijun
@File    : 函数练习.py

'''
#无参数无返回
def test():
    print("无参数无返回")

#无参数有返回
def test1():
    return 1+1

#有参数无返回
def test2(name):
    print("你好啊！！！",name)

#有参数有返回
def test3(name):
    return name

test()
print(test1())
test2("韩信")
print(test3("张良"))

#必须参数
def BMI(height,weight:int):
    if height/weight>1.2:
        print("你需要增重")
    elif height/weight>1:
        print("体重正常")
    else:
        print("您需要减肥了")
BMI(150,111)
#关键字参数  --不按照顺序传参
BMI(weight=120,height=180)
#默认参数
def emp(name,age,position,job,sex,dep_name="一部"):
    print(f"姓名：{name}\t年龄:{age}\t职级:{position}\t\t职位:{job}\t\t性别:{sex}\t所属部门:{dep_name}")
emp("张三",30,"高级","开发","男")
emp("张三",30,"高级","Java开发","男","二部")
#不定长参数
#*参数 --将多个参数基于元组方式进行存储
def sum1(*num):
    sum=0
    for x in num:
        sum=sum+x
    print(sum)
    return sum
sum1(1,2,3,11,233,255,22)

#**参数 --将多个参数基于字典方式进行存储
def sum2(**num):
    print(num)
    print(type(num))
    sum=0
    for x,y in num.items():
        print(x,y)
        sum+=y
    print(sum)
    return sum
sum2(num1=111,num2 = 222,num3=1231)

#*单独出现  --后面参数必须关键字传参
def sum3(num1,num2,*,num3):
    print(num1+num2+num3)
    return num1+num2+num3
sum3(1,2,num3=3)