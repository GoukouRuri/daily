# coding=utf-8

# 列表生成式
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
# 生成list [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用range(0, 10)
range(0, 10)
# 生成list [1x1, 2x2, 3x3, ..., 10x10]可以循环
L = []
for x in range(0, 10):
	L.append(x * x)

# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：

L_1 = [x * x for x in range(0, 10)]
print L_1

L_2 = [x * x for x in range(0, 10) if x % 2 == 0]
print L_2

# 还可以使用两层循环，可以生成全排列
print [m + n for m in 'ABC' for n in 'XYZ']

# 列出当前目录下所有文件和目录名
import os # 导入os模块，模块的概念后面讲到
print [d for d in os.listdir('.')] # os.listdir可以列出文件和目录

#for循环其实可以同时使用两个甚至多个变量，比如dict的iteritems()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print [x + '=' + y for x ,y in d.iteritems()]  # 输出['y=B', 'x=A', 'z=C']

# 最后把一个list中所有的字符串变成小写,由于非字符串类型没有lower()方法,所以需要判断类型
L = ['Hello', 'World', 'IBM', 10, None, 'Apple']
print [x.lower() for x in L if isinstance(x, str)]   # 输出['hello', 'world', 'ibm', 'apple']


# 生成器
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器（Generator）。

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))
# 如果要一个一个打印出来，可以通过generator的next()方法：
print g.next() # 每次调用指针向下移动一个
# 但是一般是循环来调取
for x in g:
	print x

# generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。例如生成斐波拉契数列
print 'generator'
def fib(max):
	n, a, b = 0, 0, 1
    	while n < max:
    		yield b
        	a, b = b, a + b  # 赋值号左右两侧, 其中把b的值赋值给a, 把a+b的值赋值给b
        	n = n + 1

print fib(6)  # 输出<generator object fib at 0x7f66cd6ea550>

for i in fib(6):
	print i






















