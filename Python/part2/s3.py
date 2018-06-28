#!/usr/bin/python
# -*- coding: utf-8 -*-

# 导入开根函数
from math import sqrt

# 导入随机函数
from random import random

# 统计程序运行时间, 引入time库
from time import clock

DARTS = 2**28                 # 定义随机抛洒点的数量, 越大越精确,程序运行时间越久
htis = 0
clock()
for i in range(1, DARTS):
	x, y = random(), random() # random() 方法返回随机生成的一个实数，它在[0,1)范围内。
	dist = sqrt(x**2 + y**2)  # 随机点到圆心的距离
	if dist <= 1:             # 统计距离不超过圆半径的点的数量
		htis +=1

pi = 4 * (htis/DARTS)         # 四分之一圆/1 = 面积比 = 落到圆里的概率
print("pi值是%s" %(pi))
print("程序运行时间是%.12g" %(clock()))
 














