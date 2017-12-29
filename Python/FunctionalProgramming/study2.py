# coding=utf-8
# 返回return
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

# 闭包的详解

def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i*i
		fs.append(f)
	return fs

# print count()  # [<function f at 0x7feca48c5668>, <function f at 0x7feca48c56e0>, <function f at 0x7feca48c5758>]

f1, f2, f3 = count()
print f1()
print f2()
print f3()
# 在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。

# 你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：9，9，9
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

# 需要先完成赋值再返回函数才能避免变量发生改变
def count(): 
	fs = []
	for i in range(1, 4):
		def f(j):
			def g():
				return j*j
			return g 
		fs.append(f(i))
	return fs

f1, f2, f3 = count()
print f1() 
print f2() 
print f3() 

















