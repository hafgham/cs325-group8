#!/usr/bin/python
#usage: python enumeration.py
###############################################################################

#function:	enum_max_sub
#args:		integer array
#returns:	max(sum of all sub arrays)
###############################################################################

def enum_max_sub(array):
	max = 0
	sum = 0
	#for each combination of i & j bounded by the length of the array
	for i in range(0, len(array)):
		for j in range(0, len(array)):
			#for non-negative ranges
			if i <= j:
				#summation of all values contained between i & j
				for k in range(i, j):
					sum = sum + array[k]
			#if new sum is larger than all previous, save
			if max < sum:
				max = sum
			#reset sum
			sum = 0
	return max


#example array from assignment - used to test algorithm.
testArray = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

print 'Testing Enumeration Function on Array:'
print testArray, '\n'
result = enum_max_sub(testArray)
print 'The maximum subarray is: ', result, '\n'
