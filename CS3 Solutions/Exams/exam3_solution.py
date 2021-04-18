import graph_AL 
import graph_AM
import graph_EL
import dsf
import matplotlib.pyplot as plt
import numpy as np
import math

def bfs(G,source=0):
    visited = [False for i in range(len(G.al))]
    prev = [-1 for i in range(len(G.al))]
    visited[source] = True
    Q = [source]
    while len(Q)>0:
        v = Q.pop(0)
        for edge in G.al[v]:
            u = edge.dest
            if not visited[u]:
                visited[u] = True
                prev[u] = v
                Q.append(u)
    return prev

def edit_distance(s1,s2):
    # Finds edit distance from s1 to s2
    # If return_array is True it will return that array containing edit distances for all substrings of s1 and s2
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    d[-1,:] = len(s2)-np.arange(len(s2)+1)  # Fill out last row
    d[:,-1] = len(s1)-np.arange(len(s1)+1)  # Fill out last column
    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s2)-1,-1,-1):
            if s1[i]==s2[j] or s1[i]=='*':
                d[i,j] =d[i+1,j+1]
            else:
                d[i,j] = 1 + min(d[i,j+1],d[i+1,j+1],d[i+1,j]) 
    return d

def is_empty_AL(G):
    for a in G.al:
        if len(a)>0:
            return False
    return True

def is_empty_AM(G):
    return np.sum(G.am) == -G.am.shape[0]*G.am.shape[1]
   
def is_empty_EL(G):
    return len(G.el)==0

def reverse_edges_EL(G):
    for edge in G.el:
        edge.source, edge.dest = edge.dest, edge.source

def reverse_edges_AM(G):
    for i in range(G.am.shape[0]):
        for j in range(i):
            G.am[i,j], G.am[j,i] = G.am[j,i], G.am[i,j]
 
def dist_from_prev(prev,u):
    if prev[u] <0:
        return 0
    return dist_from_prev(prev,prev[u])+1

def in_same_set(S,i):
    count = 0
    fi = S.find(i)
    for j in range(len(S.parent)):
        count += int(S.find(j)==fi)
    return count
            
def subsetsum2(S,goal,remain): 
    # Determines if there is a subset of S that adds up to g, where elements of S are positive integers
    # Return the subset that adds up to g if it exists or None if no such subset exists
    if goal ==0:
        return []
    if goal<0 or len(S)==0 or goal>remain:
        return None # There is no solution
    subset = subsetsum(S[1:],goal-S[0],remain-S[0]) # Take S[0]
    if subset != None: # There is a solution when taking S[0]
        return [S[0]] + subset
    else:   # There is no solution when taking S[0], try leaving S[0]
        return subsetsum(S[1:],goal,remain-S[0]) # Don't take S[0]

def subsetsum(S,goal,remain): 
    # Determines if there is a subset of S that adds up to g, where elements of S are positive integers
    # Return the subset that adds up to g if it exists or None if no such subset exists
    if goal ==0:
        return []
    if len(S)==0 :
        return None # There is no solution
    subset = subsetsum(S[1:],goal-S[0],remain-S[0]) # Take S[0]
    if subset != None: # There is a solution when taking S[0]
        return [S[0]] + subset
    else:   # There is no solution when taking S[0], try leaving S[0]
        return subsetsum(S[1:],goal,remain-S[0]) # Don't take S[0]

def have_common_characters(d):
    for i in range(1,d.shape[0]):
        for j in range(1,d.shape[1]):
            if d[i,j]==d[i-1,j-1]:
                return True
    return False


if __name__ == "__main__":   
    
    plt.close("all")   
    
    print('\n *********** Question 1 **************')   
    g = graph_AL.Graph(5)
    print(is_empty_AL(g))
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    print(is_empty_AL(g))
    
    print('\n *********** Question 2 **************')   
    g = graph_AM.Graph(5)
    print(is_empty_AM(g))
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    print(is_empty_AM(g))
    
    print('\n *********** Question 3 **************')   
    g = graph_EL.Graph(5)
    print(is_empty_EL(g))
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    print(is_empty_EL(g))
    
    print('\n *********** Question 4 **************')   
    g = graph_EL.Graph(5,directed=True)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(1,3)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
    g.draw('Question 4 initial')
    reverse_edges_EL(g)
    g.display()
    g.draw('Question 4 final')
    
    print('\n *********** Question 5 **************')   
    g = graph_AM.Graph(5,directed=True)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(1,3)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
    g.draw('Question 5 initial')
    reverse_edges_AM(g)
    g.display()
    g.draw('Question 5, final')
    
    print('\n *********** Question 6 **************')   
    g = graph_AL.Graph(5,directed=True)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(1,3)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
    g.draw('Question 6')
    p = bfs(g)
    for i in range(5):
        print('vertex',i,'distance from source',dist_from_prev(p,i))
        
    
    print('\n *********** Question 7 **************')   
    s = dsf.DSF(6)
    s.union(0,1)
    s.union(4,2)
    s.union(3,1)
    print(s.parent)
    s.draw('Question 7')
    
    for i in range(6):
        print('element',i,' elements in same set:',in_same_set(s,i))
        
    print('\n *********** Question 8 **************')   
    s = [2,5,7,11,14,-6,-10]
    for i in range(-10,10):
        print('goal:',i,'subset:',subsetsum(s,i,sum(s)))
    
    
    print('\n *********** Question 9 **************')   
    d = edit_distance('cow','pink')
    print(d)
    print(have_common_characters(d))
    d = edit_distance('cow','month')
    print(d)
    print(have_common_characters(d))
    
    
     
'''    
    g.insert_edge(1,3)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
#    Graph representation
#    directed: False, weighted: False
#    Adjacency matrix:
#    [[-1  1  1 -1 -1]
#     [ 1 -1  1  1  1]
#     [ 1  1 -1  1 -1]
#     [-1  1  1 -1  1]
#     [-1  1 -1  1 -1]]
    g.draw('Question 1 orignal')
    remove_even_odd(g)
    g.display()  
#    Graph representation
#    directed: False, weighted: False
#    Adjacency matrix:
#    [[-1 -1  1 -1 -1]
#     [-1 -1 -1  1 -1]
#     [ 1 -1 -1 -1 -1]
#     [-1  1 -1 -1 -1]
#     [-1 -1 -1 -1 -1]]
    g.draw('Question 1 result')
    
    print('\n *********** Question 2 **************')
    g = graph_AL.Graph(5,weighted=True, directed = True)
    g.insert_edge(0,1,2)
    g.insert_edge(1,2,4)
    g.insert_edge(2,3,6)
    g.insert_edge(3,4,3)
    g.insert_edge(4,0,5)
    g.display()
#    Graph representation
#    directed: True, weighted: True
#    Adjacency list:
#    al[0]=[(1,2)]
#    al[1]=[(2,4)]
#    al[2]=[(3,6)]
#    al[3]=[(4,3)]
#    al[4]=[(0,5)]
    
    g.draw('Question 2 orignal')
    reverse_edge(g,2,3)
    g.display()
    
#    Graph representation
#    directed: True, weighted: True
#    Adjacency list:
#    al[0]=[(1,2)]
#    al[1]=[(2,4)]
#    al[2]=[]
#    al[3]=[(4,3)(2,6)]
#    al[4]=[(0,5)]    
    g.draw('Question 2 result')
    
    print('\n *********** Question 3 **************')
    g = graph_AL.Graph(5,weighted=True)
    g.insert_edge(0,1,2)
    g.insert_edge(1,2,4)
    g.insert_edge(2,3,6)
    g.insert_edge(3,4,3)
    g.insert_edge(4,0,1)
    g.insert_edge(3,0,5)
    g.display()
    g.draw('Question 3')
    print(first_prim(g))    # [0, 4, 1]
    
    print('\n *********** Question 4 **************')
    s = dsf.DSF(8)
    s.union(0,1)
    s.union(7,2)
    s.union(3,5)
    s.union(1,5)
    s.union(6,2)
    print(s.parent)
    s.draw('Question 4')
    print(largest_set(s))  # 4
   
    print('\n *********** Question 5 **************')
    mySet =[2,5,8,9,12,21,33]
    print(partition(mySet))  # [[2, 5, 8, 9, 21], [12, 33]]
    mySet =[2,5,8]
    print(partition(mySet))  # None
    
    print('\n *********** Question 6 **************')
    d = edit_distance('MINERS','NERD', return_array=True)
    print(d)
    print(same_last_character(d))   # False
    d = edit_distance('MINERS','DATA STRUCTURES', return_array=True)
    print(d)
    print(same_last_character(d))   # True
    
'''
    
   
    