# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 23:38:03 2016

@author: ruialberto


def longest_run(L):

#Using two strings to represent up/down runs respectively
up_run_str, down_run_str = '', ''
for i in range(len(L) - 1):
    if L[i + 1] > L[i]:
        up_run_str += '1'
        down_run_str += ' '
    elif L[i + 1] < L[i]:
        up_run_str += ' '
        down_run_str += '1'
    else:
        up_run_str += '1'
        down_run_str += '1'

#Create two lists consist of up/down runs
up_runs = up_run_str.split()
down_runs = down_run_str.split()

#Extract the longest run
longRun = max(up_runs + down_runs)

#Determine the beginning of the longest run
up_leftEnd = up_run_str.find(longRun) % len(up_run_str)
down_leftEnd = down_run_str.find(longRun)% len(down_run_str)
leftEnd = min(up_leftEnd, down_leftEnd)

#return the value of the sum of items of the longest run
return sum(L[leftEnd: leftEnd + len(longRun) + 1])

"""
def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    #YOUR CODE HERE

    best_length = best_sum = 0
    for i in range(len(L)):
        for j in range(i, len(L)+1):
            if L[i:j] == sorted(L[i:j]) or L[i:j] == sorted(L[i:j], reverse=True):
                if j-i > best_length:
                    best_length = j-i
                    best_sum = sum(L[i:j])
    return best_sum
    
#print (max_contig_sum([8,3,4,5,7,7,7,8,2]))
#print (max_contig_sum([2,-3,1,4,6,-8,9,3])) 
print (max_contig_sum([10, 9, 8, -1]))    