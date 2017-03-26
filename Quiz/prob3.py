# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:12:46 2016

@author: ruialberto
"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
             
   songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)] 
   and max_size = 12.2, the function will return ['Roar','Wannabe','Timber']         
    """
    
    
    #print (songs)
    lista_final = []
    #tamanho = 0.0
    tamanho = 0
    
    #Adiciona o primeiro elemento da lista
    tamanho = tamanho + songs[0][2]
    #print('Tamanho: ',tamanho)
    if tamanho > max_size:
        return lista_final
    else:
        lista_final.append(songs[0][0])
        songs = songs[1:]
        
    songs.sort(key=lambda tup: tup[2]) 
    #print('Lista ddsdsdsd', songs)
    
    while tamanho < max_size:
        #print('Lista ddsdsdsd', songs)
        if len(songs) == 0:
                break
        #print()
        tamanho = tamanho + songs[0][2]
        #print('Tamanho: ', tamanho)
        if tamanho < max_size:
            lista_final.append(songs[0][0])
            if len(songs) == 0:
                break
            else:
                songs = songs[1:]
        else:
            tamanho = tamanho - songs[0][2]
            songs = songs[1:]
            
        
    return lista_final
    
            
     
    
            
#songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
#songs = [('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)]
print(song_playlist([('aa', 4, 4), ('bb', 5, 7), ('cc', 5, 6), ('dd', 2, 1)], 1) )  

        
    
    
    
    
    