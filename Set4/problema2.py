# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 15:39:06 2016

@author: ruialberto
"""
import numpy as np

def r_squared(y, estimated):
    dados_reais = np.array(y)
    estimativa = np.array(estimated)
    
    subt = estimativa - dados_reais
    p = np.power(subt,2)
    estimateError = np.sum(p)
    
    meanOfMeasure = np.sum(dados_reais)/float(len(dados_reais))
    
    variability_tmp = dados_reais - meanOfMeasure
    variability = np.sum(np.power(variability_tmp,2))
    
    return 1 - estimateError/variability
    
    
estYval = [0.07444857, 0.10270813,  0.13096769,  0.15922725,  0.18748681,  0.21574637,  0.24400593,  0.27226549,  0.30052505,  0.32878462,  0.35704418,  0.38530374,   0.4135633,   0.44182286]    

dis = [0.0865, 0.1015, 0.1106, 0.1279, 0.1892, 0.2695,0.2695, 0.2888, 0.2425, 0.3465, 0.3225, 0.3764, 0.4263, 0.4562 ]

#mass = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75]
    
#verificar_fit(mass,dis,1) 
   
print(r_squared(dis, estYval))    