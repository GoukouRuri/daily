# coding=utf-8

# 匿名函数
f = lambda x: x * x
print f             # <function <lambda> at 0x7f71902af5f0>

# 装饰器
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
	print 'Hello World'
fn = now
print fn    # 输出<function now at 0x7f71902af668>
fn()        # Hello World

# 函数对象有一个__name__属性，可以拿到函数的名字：
print f.__name__         # <lambda>
print fn.__name__        # now

# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
    print '2013-12-25'
# 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：
print now()

# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
import functools
def log(text):
	def dec(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print '%s %s():' % (text, func.__name__)
			return func(*args, **kw)  
		return wrapper
	return dec

@log('execute')
def now():
	print 'Hello Python'

now()

# 偏函数
# 在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点
def f(x, y):  # 原函数有两个参数
	print x, y
	return
# 使用偏函数
import functools

fn = functools.partial(f, y = 2)
print fn(10)

# int函数第二个参数代表将字符串作为多少位的数字进行转化
int2 = functools.partial(int, base = 2)
print int2('1010101010')  # 先转成二进制的1010101010, 在转化为十进制,所有最后输出682




























