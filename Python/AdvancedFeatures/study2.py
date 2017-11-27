# coding=utf-8

# 迭代


# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
l = range(10)
for x in l:
	print x

# list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：
# 循环dict的key
d = {'Bob': 98, 'Windy': 95, 'Athera': 100}
for key in d:
	print key

# 循环dict的value
for value in d.itervalues():
	print value

# 同时循环dict的key,value
for key, value in d.iteritems():
	print key, value
# 对list进行key,value循环
l = ['A', 'B', 'C']
for index, value in enumerate(l):
	print index, value

# 由于字符串也是可迭代对象，因此，也可以作用于for循环
s = 'Hello'
for x in s:
	print x

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
number = 10
def myfor(a):
	from collections import Iterable  # 需要先加载collections模块
	if isinstance(a, Iterable) :
		for x in a:
			print x
	else:
		print 'it\'s not iterable'

myfor(number)
myfor(s)

# 循环两个变量
# 输出
# 1 1
# 2 4
# 3 9
data = [(1, 1), (2, 4), (3, 9)]
for x, y in data:
	print x, y



















