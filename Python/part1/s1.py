# coding=utf-8

# 温度转换程序
input_temperature = input("请输入带有温度表示符号的温度值（例如32C）:")
if input_temperature[-1] in ['c', 'C']:
	f = 1.8 * float(input_temperature[0:-1]) + 32
	print("转换后的华式温度为%.2fF" %f)

elif input_temperature[-1] in ['F', 'f']:
	c = (float(input_temperature[0:-1]) - 32) / 1.8
	print("转换后的摄氏温度为%.2fC" %c)
	
else:
	print("输入有误！")


# in 二元运算符，左边的元素是否在右边的集合里
# 同步赋值语句t=x x=y y=t 直接用一行代码表示为x,y=y,x
# if elif else 条件语句








