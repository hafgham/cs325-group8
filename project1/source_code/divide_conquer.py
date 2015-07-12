#!/usr/bin/python
#usage: python divide_conquer.py
###############################################################################
from sys import maxint

#function:	divide_conquer_max_sub
#args:		integer array, length of array
#returns:	maximum sum of all subarrays
###############################################################################



def divide_conquer_max_sub(a):   

	# the following function is to find the crossiing max subarray
    def find_cross_max(a, l, r, m):

        # left Side
        ls_l = m+1
        ls_r = m
        l_max_sum = None
        sub_sum = 0
		# add elements from right to left
        for j in xrange(m,l-1,-1):
            sub_sum += a[j]
            if sub_sum > l_max_sum:
                l_max_sum = sub_sum
                ls_l = j
        
        # right Side             
        rs_l = m+1
        rs_r = m
        r_max_sum = 0
        sub_sum = 0
		# add elements from left to right
        for j in range(m+1,r+1):
            sub_sum += a[j]
            if sub_sum > r_max_sum:
                r_max_sum = sub_sum
                rs_r = j

        #combine sums
        return (ls_l, rs_r, l_max_sum+r_max_sum)
	sum = 0

    def Divide_and_conqur_recursion_classification(a,l,r):   
		
		# Base case
        if r == l:
            return (l,r,a[l])
		# Notice below that we pass array indexed starting at half_array_len
        else:

            m = (l+r)//2                    
            left_max = Divide_and_conqur_recursion_classification(a,l,m)        
            right_max = Divide_and_conqur_recursion_classification(a,m+1,r)     
			# Recursive cases
            cross_max = find_cross_max(a,l,r,m)   
			# check maximum sum left side
            if left_max[2]>=right_max[2] and left_max[2]>=cross_max[2]:
                return left_max
			# check maximum sum right side
            elif right_max[2]>=left_max[2] and right_max[2]>=cross_max[2]:
                return right_max
			# check the crossing sum 
            else:
                return cross_max

    #back to master function
    l = 0
    r = len(a)-1
	
    return Divide_and_conqur_recursion_classification(a,l,r)