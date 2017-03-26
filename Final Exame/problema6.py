# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 20:47:42 2016

@author: ruialberto
"""
import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty numpy.array of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    lista = []
    n = len(choices)
    
    #Calcula os numeros binarios
    for i in range(1<<n):
        s=bin(i)[2:] # Função bin retorna o numero binario (retirar primeiros 2 caracteres)
        s='0'*(n-len(s))+s # Acresccenta os zeros necessarios à esquerda
        list_tmp=(list (map(int,list(s))))
        lista.append(list_tmp)
        
    ch = np.array(choices)
    bi = np.array(lista)
    
    #print(ch)    
    #print(bi)
    
    for i in bi:
        print (i, '*', ch, '=', sum(i * ch) )
        if sum(i * ch) == total:
            return i
   
    #caso não encontre o resultado para o valor total
    #então executa com o valor-1, até encontrar uma solução        
    return find_combination(choices, total= total-1)
     
    
    
    
print(find_combination([1, 3, 4, 2, 5], 16))           
#print(find_combination([4, 6, 3, 5, 2], 10))        
#print(find_combination([1,1,3,5,3],5)) 
#print(find_combination([1,1,1,9],4))       
#print(find_combination([1,2,2,3],4))