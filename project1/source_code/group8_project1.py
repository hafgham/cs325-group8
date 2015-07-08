#!/usr/bin/python
#usage: python group8_project1.py <name_of_file.txt>
###############################################################################
from enumeration import enum_max_sub
from better_enum import better_enum_max_sub
from divide_conquer import divide_conquer_max_sub
from linear_time import linear_max_sub
from sys import argv
from time import sleep

# Open test file for assignment for reading
file_name = argv[1]
input_file = open(file_name, 'r')
# Save all lines of test file into a set of strings
lines = [line.translate(None, "[,]\n''") for line in input_file]
input_file.close()

testArrays = []
currentArray = []
strArray = []
# Iterate through all the lines stored from file
for i in range(0, len(lines)):
	strArray.append(lines[i].split(' '))

# Iterate through all strings stored in strArray, convert to int, and store in
# our test array
for i in range(0, len(strArray)):
	for j in range(0, len(strArray[i])):
		if(strArray[i][j] != ''):
			currentArray.append(int(strArray[i][j]))

	testArrays.append(currentArray)
	# Reset current array to empty set
	currentArray = []

algorithms = ['Enumeration', 'Better Enumeration', 'Divide and Conquer', 'Linear Time']
# Create file to write output to
file_name = 'MSS_Results.txt'
# Open file and if it exists and overwrite it
output_file = open(file_name, 'w')
output_file.write('')

# Loop through all our arrays that we are to test and test them with each algo
for i in range(0, len(testArrays)):
	output_file = open(file_name, 'a')
	output_file.write('\n========== Array %d Results ==========\n' % (i + 1))
	output_file.close()
	for j in range(0, len(algorithms)):
		print 'Testing Algorithm: ' + algorithms[j] + ' on Array ', i+1
		if(j == 0):
			result = enum_max_sub(testArrays[i])
			print 'The sum of the maximum subarray is: ', result, '\n'
			output_file = open(file_name, 'a')
			output_file.write('%d\n' % result)
			output_file.close()
		elif(j == 1):
			result = better_enum_max_sub(testArrays[i])
			print 'The sum of the maximum subarray is: ', result, '\n'
			output_file = open(file_name, 'a')
			output_file.write('%d\n' % result)
			output_file.close()
		elif(j == 2):
			result = divide_conquer_max_sub(testArrays[i], len(testArrays[i]))
			print 'The sum of the maximum subarray is: ', result, '\n'
			output_file = open(file_name, 'a')
			output_file.write('%d\n' % result)
			output_file.close()
		elif(j == 3):
			result = linear_max_sub(testArrays[i])
			print 'The sum of the maximum subarray is: ', result, '\n'
			output_file = open(file_name, 'a')
			output_file.write('%d\n' % result)
			output_file.close()

	# Pause for 1 seconds and print unless it is the last run of the loop		
	if (i + 1) < len(testArrays):
		print 'Testing next array in 1 second...\n'
		sleep(1)