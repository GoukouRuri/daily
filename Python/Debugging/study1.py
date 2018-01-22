# coding=utf-8

try:
	print 'start...'
	r = 10/0
except ZeroDivisionError, e:
	print 'except...', e
finally:
	print 'finally...'
print 'END'