# coding=utf-8

# 文件读写
# 读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的
# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，
# 我们可以使用try ... finally来实现：
try:
	f = open('./test.txt', 'r')
	print f.read()
finally:
	if f:
		f.close()


# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
# 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
with open('./test.txt', 'r') as f:
	print f.read()


# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
with open('./test.txt', 'w') as f:
    f.write('Hello, world!')
with open('./test.txt', 'r') as f:
	print f.read()

with open('./test.txt', 'a') as f:
	f.write('追加的内容');
with open('./test.txt', 'r') as f:
	print f.read()


















