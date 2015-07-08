#!/usr/bin/python
#usage: python enumeration.py
###############################################################################
from sys import maxint

#function:	enum_max_sub
#args:		integer array
#returns:	max(sum of all sub arrays)
###############################################################################
def enum_max_sub(array):
	#make max most negative possible int value
	max = -maxint - 1
	sum = 0
	index_low = 0
	index_hi = 0
	#for each combination of i & j bounded by the length of the array
	for i in range(0, len(array)):
		for j in range(0, len(array)):
			#for non-negative ranges
			if i <= j:
				#summation of all values contained between i & j
				for k in range(i, j):
					sum = sum + array[k]
			#if new sum is larger than all previous, save
			#along with the current lo and hi indices
			if max < sum:
				max = sum
				index_lo = i
				index_hi = j					
				
			#reset sum
			sum = 0
	# print the max subarray itself before returning from function
	print 'The maximum subarray is: { ',	
	for i in range(index_lo, index_hi):
		print array[i],
	print ' }'	

	return max