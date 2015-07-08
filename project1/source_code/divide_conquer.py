#!/usr/bin/python
#usage: python divide_conquer.py
###############################################################################

#function:	divide_conquer_max_sub
#args:		integer array, length of array
#returns:	maximum sum of all subarrays
###############################################################################
from sys import maxint

def divide_conquer_max_sub(array, array_len):
	# Base case
	if array_len == 1:
		return array[0]

	half_array_len = array_len / 2

	# Recursive cases
	left_max_sub = divide_conquer_max_sub(array, half_array_len)
	# Notice below that we pass array indexed starting at half_array_len
	right_max_sub = divide_conquer_max_sub(array[half_array_len:], array_len - 
		half_array_len) 

	# Initialize left and right sums to lowest possible int values
	left_sum = -maxint - 1
	right_sum = -maxint - 1
	sum = 0

	# Iterate through right half from left to right
	for i in range(half_array_len, array_len):
		sum += array[i]
		right_sum = max(right_sum, sum)
		index_hi = i

	# Reset sum and set loop driver i
	sum = 0
	i = half_array_len - 1

	# Iterate through left half from right to left
	for i in range(i, 0, -1):
		sum += array[i]
		left_sum = max(left_sum, sum)
		index_lo = i

	ans = max(left_max_sub, right_max_sub)

	return max(ans, left_sum + right_sum)

#example array from assignment - used to test algorithm.
testArray = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

print 'Testing Divide and Conquer Algorithm on Array:'
print testArray, '\n'
result = divide_conquer_max_sub(testArray, len(testArray))
print 'The sum of the maximum subarray is: ', result, '\n'