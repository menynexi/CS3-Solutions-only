import numpy as np
from math import *

def same_last_character(d):
    return d[-2,-2]==0

def edit_distance(s1,s2,return_array=False):
    # Finds edit distance from s1 to s2
    # If return_array is True it will return that array containing edit distances for all substrings of s1 and s2
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    d[-1,:] = len(s2)-np.arange(len(s2)+1)  # Fill out last row
    d[:,-1] = len(s1)-np.arange(len(s1)+1)  # Fill out last column
    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s2)-1,-1,-1):
            if s1[i] ==s2[j]:
                d[i,j] =d[i+1,j+1]
            else:
                d[i,j] = 1 + min(d[i,j+1],d[i+1,j+1],d[i+1,j]) 
    if not return_array:
        d = d[0,0]
    return d

def edit_distance_no_replacement(s1,s2,return_array=False):
    # Finds edit distance from s1 to s2
    # If return_array is True it will return that array containing edit distances for all substrings of s1 and s2
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    d[-1,:] = len(s2)-np.arange(len(s2)+1)  # Fill out last row
    d[:,-1] = len(s1)-np.arange(len(s1)+1)  # Fill out last column
    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s2)-1,-1,-1):
            if s1[i] ==s2[j]:
                d[i,j] =d[i+1,j+1]
            else:
                d[i,j] = 1 + min(d[i,j+1],d[i+1,j]) 
    if not return_array:
        d = d[0,0]
    return d
        
if __name__ == "__main__":   
        
    s1,s2 = 'MINE','ONLINE'
    print('edit_distance({},{})={}'.format(s1,s2,edit_distance(s1,s2)))
    d = edit_distance(s1,s2,return_array=True)
    print('Distance matrix')
    print(d)
    print(same_last_character(d)) 
   
    s1,s2 = 'MINER','ONLINE'
    print('edit_distance({},{})={}'.format(s1,s2,edit_distance(s1,s2)))
    d = edit_distance(s1,s2,return_array=True)
    print('Distance matrix')
    print(d)
    print(same_last_character(d)) 
    
    s1,s2 = 'MINER','ONLINE'
    print('edit_distance({},{})={}'.format(s1,s2,edit_distance(s1,s2)))
    d = edit_distance(s1,s2,return_array=True)
    print('Distance matrix')
    print(d)
    
    s1,s2 = 'MINER','ONLINE'
    print('edit_distance_no_replacement({},{})={}'.format(s1,s2,edit_distance_no_replacement(s1,s2)))
    d = edit_distance_no_replacement(s1,s2,return_array=True)
    print('Distance matrix')
    print(d)

    s1,s2 = 'SOUNDS','FOUND'
    print('edit_distance({},{})={}'.format(s1,s2,edit_distance(s1,s2)))
    d = edit_distance(s1,s2,return_array=True)
    print('Distance matrix')
    print(d)
 
    s1,s2 = 'SOUNDS','FOUND'
    print('edit_distance_no_replacement({},{})={}'.format(s1,s2,edit_distance_no_replacement(s1,s2)))
    d = edit_distance_no_replacement(s1,s2,return_array=True)
    print('Distance matrix')
    print(d)
'''
Program output 
edit_distance(MINE,ONLINE)=3
Distance matrix
[[3 2 1 1 2 3 4]
 [3 2 1 0 1 2 3]
 [4 3 2 1 0 1 2]
 [5 4 3 2 1 0 1]
 [6 5 4 3 2 1 0]]
True
edit_distance(MINER,ONLINE)=4
Distance matrix
[[4 3 2 2 3 4 5]
 [4 3 2 1 2 3 4]
 [5 4 3 2 1 2 3]
 [6 5 4 3 2 1 2]
 [6 5 4 3 2 1 1]
 [6 5 4 3 2 1 0]]
False
edit_distance(MINER,ONLINE)=4
Distance matrix
[[4 3 2 2 3 4 5]
 [4 3 2 1 2 3 4]
 [5 4 3 2 1 2 3]
 [6 5 4 3 2 1 2]
 [6 5 4 3 2 1 1]
 [6 5 4 3 2 1 0]]
edit_distance_no_replacement(MINER,ONLINE)=5
Distance matrix
[[5 4 3 2 3 4 5]
 [4 3 2 1 2 3 4]
 [5 4 3 2 1 2 3]
 [6 5 4 3 2 1 2]
 [7 6 5 4 3 2 1]
 [6 5 4 3 2 1 0]]
edit_distance(SOUNDS,FOUND)=2
Distance matrix
[[2 2 3 4 5 6]
 [2 1 2 3 4 5]
 [3 2 1 2 3 4]
 [4 3 2 1 2 3]
 [5 4 3 2 1 2]
 [5 4 3 2 1 1]
 [5 4 3 2 1 0]]
edit_distance_no_replacement(SOUNDS,FOUND)=3
Distance matrix
[[3 2 3 4 5 6]
 [2 1 2 3 4 5]
 [3 2 1 2 3 4]
 [4 3 2 1 2 3]
 [5 4 3 2 1 2]
 [6 5 4 3 2 1]
 [5 4 3 2 1 0]]   
'''