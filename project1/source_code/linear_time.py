#!/usr/bin/python
#usage: python linear_time.py
###############################################################################

#function:	linear_max_sub
#args:		integer array containing AT LEAST 1 positive integer
#returns:	maximum sum of all subarrays
###############################################################################

def linear_max_sub(array):
	ans = 0
	sum = 0

	for i in range(0, len(array)):
		if(sum + array[i] > 0):
			sum += array[i]

		else:
			sum = 0

		ans = max(ans, sum)

	return ans

#example array from assignment - used to test algorithm.
testArray = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

print 'Testing Linear Time Algorithm on Array:'
print testArray, '\n'
result = linear_max_sub(testArray)
print 'The sum of the maximum subarray is: ', result, '\n'