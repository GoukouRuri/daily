#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import *

def main():
	print("这是一个求解二次方程组实根的程序实例\n")
	a, b, c = (int(x) for x in input("求输入系数a,b,c的值: ").strip().split())
	try:
		disRoot = sqrt(b**2 - 4*a*c)
		root1 = (-b + disRoot)/(2*a)
		root2 = (-b - disRoot)/(2*a)
		if (root1 == root2):
			print("有一个实根为%d" %root1)
		else:
			print("有两个实根, 一个为%d,另一个为%d" %(root1, root2))
	except ValueError as e:
		print("没有实根,异常为:", e)

main()















