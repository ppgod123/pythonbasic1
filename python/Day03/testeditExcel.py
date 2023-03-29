# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/28 0028 上午 10:38
@Author  : fengaijun
@File    : testeditExcel.py

'''
import openpyxl

# 打开指定的Excel文件
wb = openpyxl.load_workbook('userinfo.xlsx')

# 选择需要编辑的工作表
ws = wb['Sheet1']

# 定义要插入的数据
data = [
    [1, 'apple', 2],
    [2, 'orange', 3],
    [3, 'banana', 4]
]

# 遍历数据并将它们插入到行中
for row in data:
    ws.append(row)

# 保存工作表
wb.save('userinfo.xlsx')