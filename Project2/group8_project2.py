#!/usr/bin/python
#usage: python group8_project2.py <name_of_file.txt>
###############################################################################
from changeslow import changeslow
from changegreedy import changegreedy
from changedp import changedp
from sys import argv
from sys import maxint
from time import sleep
import os
import numpy as np

# Open test file for assignment for reading
file_name = argv[1]
input_file = open(file_name, 'r')
# Save all lines of test file into a set of strings
lines = [line.translate(None, "[,]\n''") for line in input_file]
input_file.close()
print lines

testArrays = []
valueArray = []
changeArray = []
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
	#create new arrays only containing, the value list of coins,
	#or the change desired for passing to our functions later easily
	# Reset current array to empty set
	currentArray = []

valueArray = testArrays[0::2]
changeArray = testArrays[1::2]
valueArray = np.asarray(valueArray)
changeArray = np.asarray(changeArray)
#changeArray = [int(i) for i in changeArray]
print "valueArray = " , valueArray
print "changeArray = ", changeArray

algorithms = ['Brute Force', 'Greedy', 'Dynamic Programming']
# Create file to write output to
file_name = file_name.split(".")[0].split("/")[-1]
file_name += 'change.txt'
# Open file and if it exists and overwrite it
output_file = open(file_name, 'w')
output_file.write('')

# Loop through all our arrays that we are to test and test them with each algo
for i in range(0, len(changeArray)):
	output_file = open(file_name, 'a')
	output_file.write('\n========== Array %d Results ==========\n' % (i + 1))
	output_file.close()
	for j in range(0, len(algorithms)):
		print 'Testing Algorithm: ' + algorithms[j] + ' on Array ', i+1
		if j == 0:
			result = 'still testing...'
			#result = changeslow(valueArray[i], changeArray[i])
			print 'Minimum coins for Brute Force: ', result, '\n'
			output_file = open(file_name, 'a')
			output_file.write('%s\n' % result)
			output_file.close()
		elif j == 1:
			result = changegreedy(valueArray[i], changeArray[i])
			print 'Minimum coins for Greedy: ', result, '\n'
			output_file = open(file_name, 'a')
			output_file.write('%s\n' % result)
			output_file.close()
		elif j == 2:
			result = changedp(valueArray[i], changeArray[i])
			print 'Minimum coins for Dynamic Programming: ', result, '\n'
			output_file = open(file_name, 'a')
			output_file.write('%s\n' % result)
			output_file.close()

	# Pause for 1 seconds and print unless it is the last run of the loop		
	if (i + 1) < len(testArrays):
		print 'Testing next array in 1 second...\n'
		sleep(1)
