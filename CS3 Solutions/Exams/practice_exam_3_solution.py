import graph_AL 
import graph_AM
import graph_EL
import dsf
import matplotlib.pyplot as plt
import numpy as np

def is_compressed(s):
    compressed = True
    for i in range(len(s.parent)):
        if s.parent[i]>=0 and s.parent[s.parent[i]]>=0:
            print('{} is not a root and its parent is not a root'.format(i))
            compressed = False
    return compressed

def three_layer_graph(a,b,c):
    g = graph_AL.Graph(a+b+c,directed=True)
    for i in range(a):
        for j in range(a,a+b):
            g.insert_edge(i,j)
    for i in range(a,a+b):
        for j in range(a+b,a+b+c):
            g.insert_edge(i,j)      
    return g
   
def dist_from_prev(G,prev,v):
    d = 0
    while prev[v]>=0:
        d += G.am[prev[v],v]
        v = prev[v]
    return d

def in_degrees(G):
    in_deg = [0 for i in range(G.vertices)]
    for edge in G.el:
        in_deg[edge.dest]+=1
    return in_deg

def first_prim(G,source):
    fp = G.al[source][0]
    for edge in G.al[source]:
        if edge.weight<fp.weight:
            fp=edge
    return [source,fp.dest,fp.weight]

def compress(s):
    for i in range(len(s.parent)):
        if s.parent[i]>=0:
            s.parent[i]=s.find(i)
        
def subsetsum_nr(S,goal): 
    stack = [[S,goal,[]]]
    while len(stack)>0:
        r= stack.pop()
        S,goal,selection = r[0],r[1],r[2]
        if goal==0:
            return selection
        if goal>0 and len(S)>0:
            stack.append([S[1:],goal-S[0],selection+[S[0]]])
            stack.append([S[1:],goal,selection])
    return None
            
def prime(n):
    for i in range(100):
        i = np.random.randint(2,int(np.sqrt(n))+1)
        if n%i == 0:
            return False
    return True
        
def edit_distance(s1,s2):
    vowels = 'aeiouAEIOU'
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    d[-1,:] = len(s2)-np.arange(len(s2)+1)  # Fill out last row
    d[:,-1] = len(s1)-np.arange(len(s1)+1)  # Fill out last column
    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s2)-1,-1,-1):
            if s1[i] ==s2[j]:
                d[i,j] =d[i+1,j+1]
            else:
                if (s1[i] in vowels) == (s2[j] in vowels):
                    d[i,j] = 1 + min(d[i,j+1],d[i+1,j+1],d[i+1,j]) 
                else:
                    d[i,j] = 1 + min(d[i,j+1],d[i+1,j])
    return d

if __name__ == "__main__":   
    
    plt.close("all")   
    print('\n *********** Question 1 **************')
    g = three_layer_graph(3,2,3)
    g.display()

       
    print('\n *********** Question 2 **************')
    g = graph_EL.Graph(5,weighted=True,directed = True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,7)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(2,4,8)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.display()
    g.draw()
    print(in_degrees(g))   

    print('\n *********** Question 3 **************')
    g = graph_AM.Graph(5,weighted=True,directed = True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,7)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(2,4,8)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.display()
    g.draw()
    prev = [-1, 0, 1, 2, 2]
    for v in range(5):
        print('dist to {} = {}'.format(v,dist_from_prev(g,prev,v)))

    
    print('\n *********** Question 4 **************')
    g = graph_AL.Graph(6,weighted=True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,5,3)
    g.insert_edge(0,4,5)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(2,4,8)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.display()
    g.draw()
    
    print(first_prim(g,0))   
    print(first_prim(g,2))    


    print('\n *********** Question 5 **************')
    s = dsf.DSF(8)
    s.union(0,1)
    s.union(7,2)
    s.union(3,5)
    s.union(1,5)
    s.union(6,2)
    print(s.parent)         
    print(is_compressed(s)) 
    s.draw()
    compress(s)
    print(s.parent)         
    print(is_compressed(s)) 
    s.draw()
    
    print('\n *********** Question 6 **************')
    mySet =[2,5,8,9,12,21,33]
	  
    for goal in [7,15,16,20]:
        print('Goal:',goal,'  Solution:',subsetsum_nr(mySet,goal))
    
    print('\n *********** Question 7 **************')
    np.random.seed(seed=1)
    
    print(prime(11))  
    print(prime(63)) 
    print(prime(29))  
    print(prime(55))  
    
    print('\n *********** Question 8 **************')
    s1,s2 = 'MINERO','MONEY'
    d = edit_distance(s1,s2)
    
    print('edit_distance({},{})={}'.format(s1,s2,d[0,0]))   
    print('Distance matrix:')
    print(d)
    


'''
 *********** Question 1 **************
Graph representation
directed: True, weighted: False
Adjacency list:
al[0]=[3, 4]
al[1]=[3, 4]
al[2]=[3, 4]
al[3]=[5, 6, 7]
al[4]=[5, 6, 7]
al[5]=[]
al[6]=[]
al[7]=[]

 *********** Question 2 **************
Graph representation
directed: True, weighted: True
Edge list:
(0,1,4), (0,2,7), (1,2,2), (2,3,1), (2,4,8), (3,4,5), (4,1,4)
[0, 2, 2, 1, 2]

 *********** Question 3 **************
Graph representation
directed: True, weighted: True
Adjacency matrix:
[[-1  4  7 -1 -1]
 [-1 -1  2 -1 -1]
 [-1 -1 -1  1  8]
 [-1 -1 -1 -1  5]
 [-1  4 -1 -1 -1]]
dist to 0 = 0
dist to 1 = 4
dist to 2 = 6
dist to 3 = 7
dist to 4 = 14

 *********** Question 4 **************
Graph representation
directed: False, weighted: True
Adjacency list:
al[0]=[(1,4), (5,3), (4,5)]
al[1]=[(0,4), (2,2), (4,4)]
al[2]=[(1,2), (3,1), (4,8)]
al[3]=[(2,1), (4,5)]
al[4]=[(0,5), (2,8), (3,5), (1,4)]
al[5]=[(0,3)]
[0, 5, 3]
[2, 3, 1]

 *********** Question 5 **************
[-1, 0, -1, 0, -1, 3, 2, 2]
5 is not a root and its parent is not a root
False
[-1, 0, -1, 0, -1, 0, 2, 2]
True

 *********** Question 6 **************
Goal: 7   Solution: [2, 5]
Goal: 15   Solution: [2, 5, 8]
Goal: 16   Solution: [2, 5, 9]
Goal: 20   Solution: [8, 12]

 *********** Question 7 **************
True
False
True
False

 *********** Question 8 **************
edit_distance(MINERO,MONEY)=3
Distance matrix:
[[3 4 4 5 6 6]
 [4 3 3 4 5 5]
 [4 3 2 3 4 4]
 [5 4 3 2 3 3]
 [4 4 3 3 2 2]
 [4 3 3 2 2 1]
 [5 4 3 2 1 0]]
'''