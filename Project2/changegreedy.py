#!/usr/bin/python
#usage: python changegreedy.py
###############################################################################

#similar to var_dump in PHP
import pprint

#function:	changegreedy
#args:		integer array, integer
#returns:	2 element list - first element is the number of coins, the second 
#		is an array that repressents the coins used.
###############################################################################

def changegreedy(v, A):
	used = [0 for x in range(len(v))]
	num_coins = 0
	remaining = A
	#countdown loops are funky in python
	for i in range(len(v)-1, -1, -1):
		while remaining >= v[i]:
			remaining = remaining - v[i]
			used[i] = 1 + used[i]
			num_coins = 1 + num_coins
	return [num_coins, used]


test = [1, 2, 4, 8]
print 'test for v = [1, 2, 4, 8] and A = 15 returns:'
result = changegreedy(test, 15)
pprint.pprint(changegreedy(test, 15))
print 'm=', result[0]
for i in range(len(result[1])):
	print 'Number of value', test[i], 'coins is:', result[1][i]
print
test = [1, 3, 7, 12]
print 'test for v = [1, 3, 7, 12] and A = 29 returns:'
result = changegreedy(test, 29)
pprint.pprint(changegreedy(test, 29))
print 'm=', result[0]
for i in range(len(result[1])):
	print 'Number of value', test[i], 'coins is:', result[1][i]
print
test = [1, 3, 7, 12]
print 'test for v = [1, 3, 7, 12] and A = 31 returns:'
result = changegreedy(test, 31)
pprint.pprint(changegreedy(test, 31))
print 'm=', result[0]
for i in range(len(result[1])):
	print 'Number of value', test[i], 'coins is:', result[1][i]
