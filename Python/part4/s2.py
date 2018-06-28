#!/usr/bin/python
# -*- coding: utf-8 -*-

# 身体质量指数BMI程式

# s2.py
import math
import sys
weight, height = eval(input("please input your weight and height? ").split())

print(weight)
print(height)
# print eval(input("please input your weight and height? ").strip().split());
sys.exit()
bmi = height/math.pow(weight, 2)

# format格式化函数https://www.cnblogs.com/gide/p/6955895.html
print("Your BMI is {:.2f}", fornnat(bmi))














