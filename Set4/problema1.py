# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:04:21 2016

@author: ruialberto
"""

import numpy as np

def generate_models(anos, temperaturas, degs):
    
    
    x = np.array(anos)
    y = np.array(temperaturas)
    lista = []
    
    for f in degs:
        z = np.polyfit(x,y,f)
        lista.append(z)
    
    return lista
    
   

    
#print(generate_models([1961, 1962, 1963],[4.4,5.5,6.6],[1,2]))
print(generate_models([1961, 1962, 1963], [4.4, 5.5, 6.6], [1, 2]))