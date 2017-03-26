#From codereview.stackexchange.com                    

def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b


# This is a helper function that will fetch all of the available 
# partitions for you to use for your brute force algorithm.
def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]
        
        
        

### Uncomment the following code  and run this file
### to see what get_partitions does if you want to visualize it:

#for item in (get_partitions(['a','b','c','d'])):
#    print(item)

#cow={'Florence': 2, 'Henrietta': 9, 'Milkshake': 2, 'Outra': 8}
#cow = {'Miss Bella': 25, 'Lotus': 40, 'Milkshake': 40, 'Boo': 20, 'MooMoo': 50, 'Horns': 25}
#conta = 0
#for item in (get_partitions(cow.items())):
#    conta = conta + 1    
#    print(item, conta)
"""
i=1
for partition in get_partitions([6,3,2,5]):
    print (i,'--',partition)
    i=i+1
    for f in partition:
        print (sum(f))

"""

"""
def knapsack_brute_force(cow, limit):
    #import sys
   
    knapsack = []
    tmpknapsack = []
    tamanho_max = int(len(cow))
    tmp = []
    soma = 0
    tmp_carga = []
    carga = []
                
    #conta = 0
               
    for f in (get_partitions(cow.values())):
         # conta = conta+1
    #for f in (get_partitions(items)):    
        print ('Temporario Knapsack = ', tmpknapsack)
        if len(tmpknapsack) > 0 and (len(tmpknapsack) <= tamanho_max):
            knapsack = tmpknapsack
            tamanho_max = len(knapsack)
            print ('KNAPSACK: ', knapsack)
        tmp = f
        print("\n--------------------------------------------------------\n") 
        print()
        print ('Sub-item=', tmp, ' F = ', f)
        lista_somas = []
        for i in tmp:
            soma = sum(i)
            lista_somas.append(soma)
            #print ('Lista das somas: ', lista_somas)
        for s in range(len(lista_somas)):
            if lista_somas[s] > limit:
                tmpknapsack = [] 
                                    
                break
            else:
                tmpknapsack = f
                #print ('Temporario Knapsack = ', tmpknapsack)
        if len(knapsack) == 0:
            knapsack = tmpknapsack
            
    for l in knapsack:
        if len(tmp_carga) > 0:
            carga.append(tmp_carga)
            tmp_carga = []
        for l1 in l:
            for cod in cow:
                if l1 == cow[cod]:
                    tmp_carga.append(cod)
    carga.append(tmp_carga)                
      
    
    return knapsack, carga




#cow={'Florence': 2, 'Henrietta': 9, 'Milkshake': 2, 'Outra': 4} 
#cow={'Florence': 2, 'Henrietta': 9, 'Milkshake': 2, 'Herman': 7, 'Oreo': 6, 'Betsy': 9, 
cow={'Moo Moo': 3, 'Maggie': 3, 'Lola': 2, 'Millie': 5}   
#cow={'Horns': 50, 'Louis': 45, 'MooMoo': 85, 'Lotus': 10, 'Patches': 60, 'Clover': 5}
#cow = {'Betsy':65, 'Daisy':50, 'Butter':72}
#cow = {'Miss Bella': 25, 'Lotus': 40, 'Milkshake': 40, 'Boo': 20, 'MooMoo': 50, 'Horns': 25}
#cow= {'Starlight': 54, 'Buttercup': 11, 'Luna': 41, 'Betsy': 39}
print("\n Resultado final: ", knapsack_brute_force(cow,100))

"""
#for item in (get_partitions(['a','b','c','d'])):
#    print(item)


#t = list()
#for f in (get_partitions([2,9,3,7])):
#    t.append(f)  

"""
    
    
#print("\n Resultado final: ", knapsack_brute_force([2,9,2,7], 10))
    
#print("\n Resultado final: ", knapsack_brute_force([2,9,2,7,6,9], 11))
    
"""  
#cow={'Florence': 2, 'Henrietta': 9, 'Milkshake': 2}
#cow={'Florence': 2, 'Henrietta': 9, 'Milkshake': 2, 'Herman': 7, 'Oreo': 6, 'Betsy': 9, 
#'Moo Moo': 3, 'Maggie': 3, 'Lola': 2, 'Millie': 5}
"""

for item in (get_partitions(cow.values())):
    print(item)    
    
"""
"""
cow={'Florence': 2, 'Henrietta': 9, 'Milkshake': 3, 'Outra': 8}
lista = [[9], [2,3], [8,2]]
tmp_carga = []
carga = []

for l in lista:
    if len(tmp_carga) > 0:
        carga.append(tmp_carga)
        print('Carga: ', carga)
        tmp_carga = []
    for l1 in l:
        for cod in cow:
            if l1 == cow[cod]:
                tmp_carga.append(cod)
                print('TMP: ', tmp_carga)
carga.append(tmp_carga)
    
    #carga.extend(tmp)    
print ("Carga: ", carga)    

"""            
"""    
l_tuple = [[('h',3),('x',5)], [('y',2)], [('z',2), ('w',8)]]

soma_tuple = 0
tmp_tup = []
valores_somados = []
carga=[]
carga_final=[]

for f in range (len(l_tuple)):
    tmp_tup = l_tuple[f]
    for t in range(len(tmp_tup)):
        soma_tuple = soma_tuple + int(tmp_tup[t][1])
    valores_somados.append(soma_tuple) 
    soma_tuple = 0


for f in range(len(l_tuple)):
    print ('F: ', f)
    tmp_tup = l_tuple[f]
    print ('tmp_tup: ', tmp_tup)
    for t in range(len(tmp_tup)):
        carga.extend(tmp_tup[t][0])
    carga_final.append(carga) 
    carga=[]
        
    
print ('CARGA: ', carga_final)    
    
    
print('Valores somados = ',valores_somados)    
#print(l_tuple[0][0][1] + l_tuple[0][1][1], l_tuple[1][0][1])

"""
        