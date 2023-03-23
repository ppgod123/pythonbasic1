# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/14 0014 下午 5:53
@Author  : fengaijun
@File    : 循环语句.py

'''

#for循环
sum1=0
for x in range(1,101):
    sum1+=x
    #print(f"当前x值:{x}", f"当前累加总和：{sum1}")
print("0-100求和结果",sum1)
#while循环
i=0
sum2=0
while i<=100:
    sum2+=i
    #print(f"当前i值:{i}", f"当前累加总和：{sum2}")
    i+=1
print("0-100求和",sum2)

#九九乘法表
for i in  range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i} = {i*j}","\t",end="")
    print()

#打印三角形
for x in range(1,6):
    print()
    for y in range(1,x+1):
        print("*",end="")