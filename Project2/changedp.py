#!/usr/bin/python
#usage: python changedp.py
###############################################################################
from sys import maxint
#similar to var_dump in PHP
import pprint
#function:	changedp
#args:		integer array, integer
#returns:	2 element list - first element is the number of coins, the second is an array that repressents the coins used.
###############################################################################

def changedp(v, A):
	#2D list to hold the specific coins used for each amount
	selected_coins = [[0 for x in range(len(v))] for y in range (A+1)]
	#list to hold the number of coins used for each amount
	num_coins_used = [0 for x in range(A+1)] 
	#base case: zero amount takes zero coins
	num_coins_used[0] = 0
	#for every Amount(A) > 1, including the amount were actually iterested in
	for i in range(1, A+1):
		#essentially, what we are doin here is testing if the currnt coin were on is les than or equal to the current amount we're calculating(i.e. if we have a coin that has a value of 5 and we're trying to find the number of coins it takes to make 4, then we would skip that coin) an we're testing if (the number of coins it takes to make the Amount[for the current Amount less the value of the current coin] + 1) is less than the curen. If this is the case, then i means that a coin of the current value can in fact be added to that Amount and it the Amount wil lbe less than or equal to the amount that we are currently interested in. (This took me a really long time to wrap my head around)
		num_coins_used[i] = maxint
		#for every coin value
		for j in range(0, len(v)):
			if (i >= v[j]) and ((1+num_coins_used[i-v[j]])<num_coins_used[i]):
				num_coins_used[i] = 1 + num_coins_used[i-v[j]]
				#here we copy the coins used to create the amount for the subproblem
				for k in range(len(v)):
					selected_coins[i][k] = selected_coins[i-v[j]][k]
				#here we increment the coin we used
				selected_coins[i][j] = 1 + selected_coins[i][j]

	#return a jagged list, the first element being the number of coins used for A, the second being a list of which coins are used
	return [num_coins_used[A], selected_coins[A]]


test = [1, 2, 4, 8]
print 'test for v = [1, 2, 4, 8] and A = 15 returns:'
result = changedp(test, 15)
pprint.pprint(changedp(test, 15))
print 'm=', result[0]
for i in range(len(result[1])):
	print 'Number of value', test[i], 'coins is:', result[1][i]
print
test = [1, 3, 7, 12]
print 'test for v = [1, 3, 7, 12] and A = 29 returns:'
result = changedp(test, 29)
pprint.pprint(changedp(test, 29))
print 'm=', result[0]
for i in range(len(result[1])):
	print 'Number of value', test[i], 'coins is:', result[1][i]
print
test = [1, 3, 7, 12]
print 'test for v = [1, 3, 7, 12] and A = 31 returns:'
result = changedp(test, 31)
pprint.pprint(changedp(test, 31))
print 'm=', result[0]
for i in range(len(result[1])):
	print 'Number of value', test[i], 'coins is:', result[1][i]