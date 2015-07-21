# usage: python changeslow.py
###############################################################################
from sys import maxint
#function:	changeslow
#args:		integery array, integer
#returns:	array with number of each coin needed to make requested change,
#		and the minimum number of coins to make change on the next line.
###############################################################################
import pprint

def changeslow(value, change):
	if change == 0:
		return 0
	min_coins = maxint
	
	#for each value in the array, if it's less than the amount of change 
	#we want to make then we call changeslow() recursively, subtracting 
	#that value from the goal value each iteration selects the minimum 
	#number between the two, such that after rebuilding the solution, 
	#the smallest number of coins needed to make that amount of change is
	#assigned to the 'min_coins' variable. 
	used = [0 for x in range(len(value))] # initialize array to all 0's
	for i in range(0, len(value)):
		if(value[i] <= change):
			change = change - (value[i])
			min_coins = min(min_coins, changeslow(value, change) + 1)
	return min_coins

# should return '2' when run, i.e. [0, 1, 1, 0] for this test array
#testValues = [1, 5, 10, 25]
#result = changeslow(testValues, 15)
#print result
