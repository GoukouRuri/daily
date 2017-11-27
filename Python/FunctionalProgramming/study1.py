# coding=utf-8

# Python内建了map()和reduce()函数

# map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
# 比如我们有一个函数f(x)=x^2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：

def f(x):
	return x * x

L = map(f, range(0, 10))
print L  # 输出[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

# 比如对一个序列进行求和
def add(x, y):
	return x + y
print reduce(add, [1, 3, 5, 7, 9]) # 输出25
# 或者是将序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x, y):
	return x * 10 + y
print reduce(fn, [1, 3, 5, 7, 9])  # 输出13579

# Python内建的filter()函数用于过滤序列。

# 取出奇数，过滤偶数
def is_odd(x):
	return x % 2 == 1

print filter(is_odd, range(0,10)) # 输出[1, 3, 5, 7, 9]
# 过滤序列中的空字符
def not_empty(x):
	return x and x.strip()
print filter(not_empty, 'Hello World')	# 输出HelloWorld


# Python内置的sorted()函数就可以对list进行排序
print sorted([36, 5, 12, 9, 21])

# 此外，sorted()函数也是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序。比如，如果要倒序排序，我们就可以自定义一个reversed_cmp函数：
# 对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1
def desc_sort(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

print sorted([36, 5, 12, 9, 21], desc_sort)

# 返回return
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。










































