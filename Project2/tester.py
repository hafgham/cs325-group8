#!/usr/bin/python
#usage: python tester.py
###############################################################################

from changedp import changedp 
from changegreedy import changegreedy 
#from changeslow import changeslow
from changeslow_Jesse import changeslow 
import pprint, datetime

###############################################################################
#NOTE: Uncomment sections for functionality.
###############################################################################

#Question 4:

#V1 = [1, 5, 10, 25, 50]
#
#print 'Testing arrays:'
#print 'array1:'
#pprint.pprint(V1)
#
#print 'A', "\t", 'dp1', "\t", 'greed1'
#for i in range(2000, 2201):
#	dp1 = changedp(V1, i)
#	greed1 = changegreedy(V1, i)
#	print i, "\t", dp1[0], "\t", greed1[0]
#
#
#print 'A', "\t", 'dp1', "\t", 'greed1', "\t", 'slow1'
#for i in range(10, 36):
#	dp1 = changedp(V1, i)
#	greed1 = changegreedy(V1, i)
#	slow1 = changeslow(V1, i)
#	print i, "\t", dp1[0], "\t", greed1[0], "\t", slow1

#Question 5:
#V1 = [1, 2, 6, 12, 24, 48, 60]
#V2 = [1, 6, 13, 37, 150]
#print 'Testing arrays:'
#print 'array1:'
#pprint.pprint(V1)
#print 'array2:'
#pprint.pprint(V2)
#print 'A', "\t", 'dp1', "\t", 'dp2', "\t", 'greed1', "\t", 'greed2'
#for i in range(2000, 2201):
#	dp1 = changedp(V1, i)
#	dp2 = changedp(V2, i)
#	greed1 = changegreedy(V1, i)
#	greed2 = changegreedy(V2, i)
#
#	print i, "\t", dp1[0], "\t", dp2[0], "\t", greed1[0], "\t", greed2[0]
#
#
#print 'A', "\t", 'dp1', "\t", 'dp2', "\t", 'greed1', "\t", 'greed2', "\t", '#slow1', "\t", 'slow2'
#for i in range(10, 40):
#	dp1 = changedp(V1, i)
#	dp2 = changedp(V2, i)
#	greed1 = changegreedy(V1, i)
#	greed2 = changegreedy(V2, i)
#	slow1 = changeslow(V1, i)
#	slow2 = changeslow(V2, i)
#	print i, "\t", dp1[0], "\t", dp2[0], "\t", greed1[0], "\t", greed2[0], "\t", slow1, "\t", slow2	


#Question 6:
#V1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
#
#print 'Testing arrays:'
#print 'array1:'
#pprint.pprint(V1)
#
#print 'A', "\t", 'dp1', "\t", 'greed1'
#for i in range(2000, 2201):
#	dp1 = changedp(V1, i)
#	greed1 = changegreedy(V1, i)
#	print i, "\t", dp1[0], "\t", greed1[0]
#
#
#print 'A', "\t", 'dp1', "\t", 'greed1', "\t", 'slow1'
#for i in range(10, 29):
#	dp1 = changedp(V1, i)
#	greed1 = changegreedy(V1, i)
#	slow1 = changeslow(V1, i)
#	print i, "\t", dp1[0], "\t", greed1[0], "\t", slow1

###############################################################################
#This section is for calculating running times:
###############################################################################

#exe time test arrary:
V1 = [1, 2, 6, 12, 24, 48, 60]
###############################################################################

#print 'For DP algo:'
#print 'A \t time'
#for i in range(0, 300001, 5000):
#	t1 = datetime.datetime.now()
#	dp1 = changedp(V1, i)
#	t2 = datetime.datetime.now()
#	diff = t2 - t1
#	print i, "\t", ((diff.seconds*1000) + int(diff.microseconds/1000))

#print 'For Greedy algo:'
#print 'A \t time'
#for i in range(0, 300000001, 5000000):
#	t1 = datetime.datetime.now()
#	dp1 = changegreedy(V1, i)
#	t2 = datetime.datetime.now()
#	diff = t2 - t1
#	print i, "\t", ((diff.seconds*1000) + int(diff.microseconds/1000))

#print 'For Slow algo:'
#print 'A \t time'
#for i in range(0, 31, 2):
#	t1 = datetime.datetime.now()
#	dp1 = changeslow(V1, i)
#	t2 = datetime.datetime.now()
#	diff = t2 - t1
#	print i, "\t", ((diff.seconds*1000) + int(diff.microseconds/1000))