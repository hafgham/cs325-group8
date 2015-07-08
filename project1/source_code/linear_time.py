#!/usr/bin/python
#usage: python linear_time.py
###############################################################################

#function:	linear_max_sub
#args:		integer array containing AT LEAST 1 positive integer
#returns:	maximum sum of all subarrays
###############################################################################
def linear_max_sub(array):
	maximum = 0
	sum = 0

	for i in range(0, len(array)):
		if(sum + array[i] > 0):
			sum += array[i]

		else:
			sum = 0

		maximum = max(maximum, sum)

	return maximum