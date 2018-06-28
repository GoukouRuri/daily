# coding=utf-8

# 绘制蟒蛇实例
# 引入turtle图像绘制库

import turtle


def drawSnake(rad, angle, len, neckrad):
	for i in range(len):
		turtle.circle(rad, angle)
		turtle.circle(-rad, angle)
	turtle.circle(rad, angle/2)
	turtle.fd(rad)
	turtle.circle(neckrad + 1, 180)
	turtle.fd(rad*2/3)

def main():
	turtle.setup(1300, 800, 0, 0)
	pythonsize = 30
	turtle.pensize(pythonsize)
	turtle.pencolor("blue")
	turtle.seth(-40)
	drawSnake(40, 80, 5, pythonsize/2)

main() #启动程序


# python对库函数的引用方式有两种
# 第一种：
# import <库名>
# import turtle
# tuttle fd(100)  #使用库里函数
# 
# 第二种
# from <库名> import <函数名>
# from turtle import fd 或者from turtle import * 
# fd(100)  # 直接使用函数







