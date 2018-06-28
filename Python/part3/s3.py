#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
	sum, count = 0, 0
	moredata = 'y'
	while moredata == 'y':
		x = eval(input('Please enter a number >> '))
		sum += x
		count += 1
		moredata = input('Do you have more numbers to enter? (y or n) ')
	print("平均值为%.2f" %(sum/count))
main()
