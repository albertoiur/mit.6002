# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 20:20:56 2016

@author: ruialberto
"""

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    soma_temp = 0.0
    lista_final = []
    
    for f in L:
        mult = s
        while (mult >= 0):
            if ((mult * f) + soma_temp) <= s:
                lista_final.append(mult)
                #print(lista_final)
                soma_temp = soma_temp + (mult * f)
                #print('SOMA:',soma_temp)
                #print()
                break
            else:
                mult = mult - 1
                
            
                    
    if soma_temp == s:
        return sum(lista_final)
    else:
        return "no solution"
        
print(greedySum([101, 51, 11, 2, 1], 3000))        