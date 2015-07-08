#!/usr/bin/python
#usage: python better_enum.py
###############################################################################

#function:	better_enum_max_sub
#args:		integer array
#returns:	max(sum of all sub arrays)
###############################################################################
from sys import maxint

def better_enum_max_sub(array):
	max = -maxint - 1
	index_lo = 0
	index_hi = 0
	#for each combination of i & j where i < j
	for i in range(0, len(array)):
		#reset sum
		sum = 0
		#calculate a continuous sum, and check sum at each addition
		for j in range(i, len(array)):
			sum = sum + array[j]
			#if new sum is larger than all previous, save
			if max < sum:
				max = sum
				index_lo = i
				index_hi = j+1 

	print 'The maximum subarray is: { ',
        for i in range(index_lo, index_hi):
                print array[i],
        print ' } \n'

	return max


#example array from assignment - used to test algorithm.
testArray = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

print 'Testing Better Enumeration Function on Array:'
print testArray, '\n'
result = better_enum_max_sub(testArray)
print 'The sum of the maximum subarray is: ', result, '\n'