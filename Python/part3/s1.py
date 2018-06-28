#!/usr/bin/python
# -*- coding: utf-8 -*-

# python2写法
# try:
# 	print 'start...'
# 	r = 10/0
# except ZeroDivisionError, e:
# 	print 'except...', e
# finally:
# 	print 'finally...'
# print 'END'

# python3写法
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')














