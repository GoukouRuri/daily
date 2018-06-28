#!/usr/bin/python
# -*- coding: utf-8 -*-

# Procedures for banks to calculate interest

# Calculation of principal and interest and function
def calculateInterest(original_amount, rate, year):
	new_amount = (1 + rate/100 * int(year)) * original_amount
	return new_amount

# Handle multiple calculated functions
def main():
	intest_list = []
	add_lock = "y"
	while add_lock == "y":
		tmp_list = [float(x) for x in input('Please enter the original_amount and rate and year separated by spaces>>').strip().split()]
		# simple verification of the input
		if (type(tmp_list[-1]) != 'int' and int(tmp_list[-1]) < 1 ):
			print("Please enter a positive integer as deposit years")
			continue
		intest_list.append(tmp_list)
		add_lock = input("Do you want add more data to calculate?(y or n) ")
	for key, value in enumerate(intest_list):
		new_amount = calculateInterest(value[0], value[1], value[2])
		value[0] = float(value[0])
		value[1] = float(value[1])
		value[2] = float(value[2])
		new_amount = float(new_amount)
		print("The %d calculation results: the principal is %d, the interest rate is %.2f%%, the year is %d, so that the sum of principal and interest is %.2f" %(key, value[0],(value[1]), value[2], new_amount))
main()
















































