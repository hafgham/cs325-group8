#!/usr/bin/python
#usage: python tester.py
###############################################################################

from changedp import changedp 
from changegreedy import changegreedy 
#from changeslow import changeslow
from changeslow_Jesse import changeslow 
import pprint
V1 = [1, 2, 6, 12, 24, 48, 60]
V2 = [1, 6, 13, 37, 150]
print 'Testing arrays:'
print 'array1:'
pprint.pprint(V1)
print 'array2:'
pprint.pprint(V2)
print 'A', "\t", 'dp1', "\t", 'dp2', "\t", 'greed1', "\t", 'greed2'
for i in range(2000, 2201):
	dp1 = changedp(V1, i)
	dp2 = changedp(V2, i)
	greed1 = changegreedy(V1, i)
	greed2 = changegreedy(V2, i)

	print i, "\t", dp1[0], "\t", dp2[0], "\t", greed1[0], "\t", greed2[0]


print 'A', "\t", 'dp1', "\t", 'dp2', "\t", 'greed1', "\t", 'greed2', "\t", 'slow1', "\t", 'slow2'
for i in range(10, 40):
	dp1 = changedp(V1, i)
	dp2 = changedp(V2, i)
	greed1 = changegreedy(V1, i)
	greed2 = changegreedy(V2, i)
	slow1 = changeslow(V1, i)
	slow2 = changeslow(V2, i)
	print i, "\t", dp1[0], "\t", dp2[0], "\t", greed1[0], "\t", greed2[0], "\t", slow1, "\t", slow2	