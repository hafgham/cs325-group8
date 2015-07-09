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
	index_low = 0
	index_hi = 0
	#for each combination of i & j bounded by the length of the array
	for i in range(0, len(array)):
		for j in range(0, len(array)):
			#for non-negative ranges
			sum = 0
			if i <= j:
				#summation of all values contained between i & j
				for k in range(i, j+1):
					sum = sum + array[k]
			#if new sum is larger than all previous, save
			#along with the current lo and hi indices
			if sum > max:
				max = sum
				index_lo = i
				index_hi = j					
				
			#reset sum
			

	# print the max subarray itself before returning from function
	print 'The maximum subarray is: { ',	
	for i in range(index_lo, index_hi):
		print array[i],
	print ' }'	

	# Build the subarray string to print to file
	array_as_string = '['
	for i in range(index_lo, index_hi):
		array_as_string += str(array[i])
		if (i + 1) < index_hi:
			array_as_string += ', '
	array_as_string += ']\n'

	# Write to file max subarray
	file_name = 'MSS_Results.txt'
	output_file = open(file_name, 'a')
	output_file.write(array_as_string)
	output_file.close()

	return max