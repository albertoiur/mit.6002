###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    lista_valores = []
    carregamento = []
    cow_backup = cows.copy()
    
          
    for c in cow_backup:
        lista_valores.append(cow_backup[c])
        
    lista_valores.sort(reverse=True)
           
    contador = 1
    tmp = []
    
    while True:
        
        for k,v in cow_backup.items():
            tmp.append(v)
        
        contador = sum(tmp)
        if contador == 0:
            break
        
        minimo = min(tmp)
        if limit < minimo:
            return carregamento
            break
        
        for j in cow_backup:
            if cow_backup[j] > limit:
                cow_backup[j] = 0
                
        
        tmp = []    
        resultado_final = [] 
        soma = 0
        x = 0
        while (x < len(lista_valores)):
            for f in lista_valores:
                #print ("Valor: ",f)
                for j in cow_backup:
                    #print ('Item Dicionario: ', cow[j])
                    if cow_backup[j] == f:
                        soma = soma + int(cow_backup[j])
                        #print ('Soma: ', soma)
                        if soma <= limit:
                            resultado_final.append(j)
                            cow_backup[j] = 0
                        else:
                            soma = soma - int(cow_backup[j])
                            x = x + 1
                    else:
                        x = x + 1
        #print (cow_backup)            
        carregamento.append(resultado_final)
                        
       
    return carregamento


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    knapsack = []
    tmpknapsack = []
    tamanho_max = int(len(cows.values()))
    #print(tamanho_max)
    tmp = []
    #soma = 0
    tmp_carga = []
    carga = []
    tmp_tup = []
    
    for f in (get_partitions(cows.items())):
        
        #print ('Temporario Knapsack = ', tmpknapsack)
        if len(tmpknapsack) > 0 and (len(tmpknapsack) <= tamanho_max):
            knapsack = tmpknapsack
            tamanho_max = len(knapsack)
            #print ('KNAPSACK: ', knapsack)
        tmp = f
        #print("\n--------------------------------------------------------\n") 
        #print()
        #print ('Sub-item=', tmp)
        soma_tuple = 0
        tmp_tup = []
        valores_somados = []
    
        for f in range (len(tmp)):
            tmp_tup = tmp[f]
            for t in range(len(tmp_tup)):
                soma_tuple = soma_tuple + int(tmp_tup[t][1])
            valores_somados.append(soma_tuple) 
            soma_tuple = 0
        #print ('Lista das somas: ', valores_somados)
        for s in range(len(valores_somados)):
            if valores_somados[s] > limit:
                tmpknapsack = [] 
                break
            else:
                tmpknapsack = tmp
               # print ('Temporario Knapsack = ', tmpknapsack)
        if len(knapsack) == 0:
            knapsack = tmpknapsack
    
    
    for f in range(len(knapsack)):
        tmp_tup = knapsack[f]
        for t in range(len(tmp_tup)):
            tmp_carga.append(tmp_tup[t][0])
        carga.append(tmp_carga)   
        tmp_carga=[]
        
        
    return carga
        
    
#Problem 3           
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    print ('------- Rui Alberto Duarte Oliveira -------------------')
    print ('------- Algoritmos Optimização --------------------\n')   
    start = time.time()
    resultado_greedy = greedy_cow_transport(cows, limit)
    end = time.time()  
    print ('\nTempo decorrido Greedy = ', end - start)
    print ('Numero Viagens Greedy = ',len(resultado_greedy), resultado_greedy)
    
    start = time.time()
    resultado_brute = brute_force_cow_transport(cows, limit)
    end = time.time()  
    print('\nTempo decorrido Brute Force = ', end - start)
    print('Numero Viagens Brute  = ', len(resultado_brute), resultado_brute)
    

    """
    Here is some test data for you to see the results of your algorithms with. 
    Do not submit this along with any of your answers. Uncomment the last two
    lines to print the result of your problem.
    """

cows = load_cows("ps1_cow_data.txt")
#cows={'Florence': 2, 'Henrietta': 9, 'Milkshake': 2, 'Outra': 4} 
#cows={'Miss Bella': 25, 'Lotus': 40, 'Milkshake': 40, 'Boo': 20, 'MooMoo': 50, 'Horns': 25}
#cows={'Betsy': 65, 'Buttercup': 72, 'Daisy': 50}
#cows={'Buttercup': 11, 'Betsy': 39, 'Starlight': 54, 'Luna': 41}
#cows={'Florence': 2, 'Henrietta': 9, 'Milkshake': 2, 'Herman': 7, 'Oreo': 6, 'Betsy': 9, 
#'Moo Moo': 3, 'Maggie': 3, 'Lola': 2, 'Millie': 5}
limit=43
print(cows)
print()
compare_cow_transport_algorithms()

#print(greedy_cow_transport(cows, limit))
#print()

#print("Resultado Final: ", brute_force_cow_transport(cows, limit))



