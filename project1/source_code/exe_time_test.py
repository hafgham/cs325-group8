#!/usr/bin/python
#usage: python exe_time_test.py [n]
###############################################################################

from random import randint
import sys, datetime
from sys import maxint

#copy/paste function instead of import to remove print and file operations
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
	#***This return is used in execution time testing***
	return max	

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

	#***This return is used in execution time testing***
	return max


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




print 'Generating array of size: ', sys.argv[1]

test_array = []
for i in range(0, int(sys.argv[1])):
	test_array.append(randint(-99,99))

#print 'Testing enumeration method...'
#t1 = datetime.datetime.now()
#enum_max_sub(test_array)
#t2 = datetime.datetime.now()
#diff = t2 - t1
#print 'Execution time: ', diff.seconds, 's', int(diff.microseconds/1000), 'ms'

#print 'Testing better enumeration method...'
#t1 = datetime.datetime.now()
#better_enum_max_sub(test_array)
#t2 = datetime.datetime.now()
#diff = t2 - t1
#print 'Execution time: ', diff.seconds, 's', int(diff.microseconds/1000), 'ms'

#print 'Testing D&C method...'
#t1 = datetime.datetime.now()
#divide_conquer_max_sub(test_array, len(test_array))
#t2 = datetime.datetime.now()
#diff = t2 - t1
#print 'Execution time: ', diff.seconds, 's', int(diff.microseconds/1000), 'ms'

print 'Testing linear method...'
t1 = datetime.datetime.now()
linear_max_sub(test_array)
t2 = datetime.datetime.now()
diff = t2 - t1
print 'Execution time: ', diff.seconds, 's', int(diff.microseconds/1000), 'ms'