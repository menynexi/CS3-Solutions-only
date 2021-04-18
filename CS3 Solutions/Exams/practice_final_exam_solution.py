import numpy as np
import matplotlib.pyplot as plt
import math
import singly_linked_list as sll
import bst
import btree
import graph_AL
import graph_AM
import graph_EL
import hash_table_chain as htc

def smaller(L,i):
    if len(L)==0:
        return []
    s = smaller(L[1:],i)
    if L[0]<i:
        s.append(L[0])
    return s

def remove_second(L):
    if L.head == None or L.head == L.tail:
        return
    L.head.next = L.head.next.next    
    if L.head.next == None:
        L.tail = L.head 
        
def cumulative_sum(L):
    C = sll.List()
    t = L.head
    cumsum=0
    while t !=None:
        cumsum+= t.data
        C.append(cumsum)
        t=t.next
    return C

def equal_row(a):
    eq = []
    va = np.var(a,axis=1)
    for i in range(a.shape[0]):
        if va[i]==0:
            eq.append(i)
    return eq
      
def sorted_rows(a):
    sorted_row = []
    for i in range(a.shape[0]):
        if np.all(a[i,1:]>=a[i,:-1]):
            sorted_row.append(i)
    return sorted_row
        
def max_at_depth_bst(T,d):
    if T == None:
        return -math.inf
    if d == 0:
        return T.data
    m = max_at_depth_bst(T.right,d-1) 
    if m> -math.inf:
        return m
    return max_at_depth_bst(T.left,d-1) 

def in_leaves(T):
    if T == None:
        return []
    if T.left == None and T.right == None:
        return [T.data]
    return in_leaves(T.left)+in_leaves(T.right)

def max_at_depth_btree(T,d):
    if d == 0:
        return T.data[-1]
    if T.is_leaf:
        return -math.inf
    return max_at_depth_btree(T.child[-1],d-1)
   
def internal(T):
    if T.is_leaf:
        return []
    internal_data = []
    for i in range(len(T.data)):
        internal_data += internal(T.child[i])
        internal_data.append(T.data[i])
    internal_data += internal(T.child[-1])
    return internal_data

def find_sum_pair(S,k):
    h = htc.HashTableChain(len(S))
    for s in S:
        if h.retrieve(k-s)!=None:
            return True
        else:
            h.insert(s,s)
    return False

def remove_duplicates(L):
    h = htc.HashTableChain(len(L))
    Lrd = []
    for i in L:
        if h.insert(i,' ')!=-1:
            Lrd.append(i)
    return Lrd

def clique(G,u,v,w):
    return min([G.am[u,v],G.am[u,w],G.am[v,w]])>-1
   
def first_ts(G):
    f = [v for v in range(len(G.al))]
    for u in range(len(G.al)):
        for edge in G.al[u]:
            try:
                f.remove(edge.dest)
            except:
                pass           
    return f

def make_undirected(G):
    G.am = np.maximum(G.am,G.am.T)
    G.directed = False
    
def make_weighted(G):
    G.weighted = True
    for i in range(len(G.al)):
        for edge in G.al[i]:
            edge.weight = i+edge.dest

def make_undirected(G):
    G.am = np.maximum(G.am,G.am.T)
    G.directed = False
    
def am_to_el(g):
    g2 = graph_EL.Graph(g.am.shape[0],directed =g.directed,weighted=g.weighted)
    for i in range(g.am.shape[0]):
        start =0 
        if not g.directed:
            start = i
        for j in range(start,g.am.shape[0]):
            if g.am[i,j]>-1:
                g2.insert_edge(i, j, g.am[i,j])
    return g2

def subsetsum_count(S,g):
    if g==0:
        return 1
    if g<0 or len(S)==0:
    	return 0
    return subsetsum_count(S[1:],g-S[0]) + subsetsum_count(S[1:],g) 

def edit_distance_with_wildcard(s1,s2):
    # Finds edit distance from s1 to s2
    # If return_array is True it will return that array containing edit distances for all substrings of s1 and s2
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    d[-1,:] = len(s2)-np.arange(len(s2)+1)  # Fill out last row
    d[:,-1] = len(s1)-np.arange(len(s1)+1)  # Fill out last column
    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s2)-1,-1,-1):
            if s1[i]==s2[j] or s1[i]=='*' or s2[j]=='*':
                d[i,j] =d[i+1,j+1]
            else:
                d[i,j] = 1 + min(d[i,j+1],d[i+1,j+1],d[i+1,j]) 
    return d    

if __name__ == "__main__":
    plt.close("all") 
    draw_figs = False # Change to True to output figures to screen
    print('================ Question 1 ===============')
    L2 =  [1, 7, 4, 3, 0, 9, 2, 5, 8, 6]
    print(smaller(L2,3))    
    print(smaller(L2,6))    
    print(smaller(L2,9))    
    
    print('================ Question 2 ===============')
    L3a = sll.List()
    L3b = sll.List()
    L3c = sll.List()
    L3d = sll.List()
    L3b.extend([5])
    L3c.extend([7,8])
    L3d.extend([3, 0, 9, 2, 5])
    for L in [L3a,L3b,L3c,L3d]:  # Show original lists
        L.print()
        if draw_figs:
            L.draw('Original list')
    
    for L in [L3a,L3b,L3c,L3d]:  
        remove_second(L)
    
    for L in [L3a,L3b,L3c,L3d]:  # Show modified lists
        L.print()
        if draw_figs:
            L.draw('Original list')
        
    print('================ Question 3 ===============')
    L3a = sll.List()
    L3b = sll.List()
    L3c = sll.List()
    L3d = sll.List()
    L3b.extend([5])
    L3c.extend([7,8])
    L3d.extend([3, 0, 9, 2, 5])
    for L in [L3a,L3b,L3c,L3d]:  # Show original lists
        L.print()
        if draw_figs:
            L.draw('Original list')
       
    for L in [L3a,L3b,L3c,L3d]:  # Show cumulative sums
        C = cumulative_sum(L)
        C.print()
        if draw_figs:
            L.draw('cumulative sum list')
        
    print('================ Question 4 ===============')
    A1 = np.array([[1],[2],[3]])
    A2 = np.array([[1,3],[2,2],[3,5],[7,7]])
    A3 = np.array([[1,3,5],[2,2,12],[3,3,3],[7,8,7],[5,8,7]])
    A4 = np.array([[1,3,5,6],[2,2,2,1],[3,3,5,6],[7,8,7,6],[5,8,7,2]])
    print('Original arrays')
    for a in [A1,A2,A3,A4]:  # Show arrays
        print(a)
    print('Results')
    for a in [A1,A2,A3,A4]:  # Show results
        print(equal_row(a))    
        
    print('================ Question 5 ===============')
    A1 = np.array([[1],[2],[3]])
    A2 = np.array([[1,3],[12,2],[3,5],[7,7]])
    A3 = np.array([[1,3,5],[2,2,12],[3,3,3],[7,8,7],[5,8,7]])
    A4 = np.array([[1,31,5,6],[2,2,2,1],[3,13,5,6],[7,18,7,6],[5,8,7,2]])
    print('Original arrays')
    for a in [A1,A2,A3,A4]:  # Show arrays
        print(a)
    print('Results')    
    for a in [A1,A2,A3,A4]:  # Show results
        print(sorted_rows(a)) 
        
    print('================ Question 6 ===============')
    L6 =[11, 6, 7, 16, 2, 4, 14, 8, 15, 1,  13,0]
    T = bst.BST()
    for a in L6:
        T.insert(a)
    if draw_figs:
        T.draw()
    for i in range(6):
        print('depth:{}, max:{}'.format(i,max_at_depth_bst(T.root,i)))
        
    print('================ Question 7 ===============')
    L5 =[11, 6, 7, 16, 2, 4, 14, 8, 15, 1,  13,0]
    T = bst.BST()
    for a in L5:
        T.insert(a)
    if draw_figs:
        T.draw()
    print(in_leaves(T.root))   
    
    print('================ Question 8 ===============')
    T = btree.BTree()
    L7 = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
  
    t = T.find(4)
    for n in L7:
        T.insert(n) 
    if draw_figs:
        T.draw()
    
    for i in range(4):
        print('depth:{}, max:{}'.format(i,max_at_depth_btree(T.root,i)))
        
    print('================ Question 9 ===============')
    T = btree.BTree()
    L7 = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
  
    t = T.find(4)
    for n in L7:
        T.insert(n) 
    if draw_figs:
        T.draw()
    print(internal(T.root)) 
    
    print('================ Question 10 ===============')
    S = [1,2,3,4,6,7]
    for i in range(15):
        print(i,find_sum_pair(S,i))
   
    print('================ Question 11 ===============')
    print(remove_duplicates([4,2,7,9,7,8,1,9,2,4]))   
    print(remove_duplicates([4,2,7,9,9,2,4]))         
    print(remove_duplicates([2,2,4,4,4,2,4,4,2]))     
    print(remove_duplicates([2302]))                  
    print(remove_duplicates([]))                      
    
    print('================ Question 12 ===============')
    g8 = graph_AM.Graph(5)
    g8.insert_edge(0,1)
    g8.insert_edge(1,2)
    g8.insert_edge(1,3)    
    g8.insert_edge(0,3)
    g8.insert_edge(2,3)
    g8.insert_edge(3,4)
    g8.insert_edge(2,4)
    g8.display()
    if draw_figs:
        g8.draw()
    
    for i in range(5):
        for j in range(i+1,5):
            for k in range(j+1,5):
                print('(u,v,w) = ({},{},{}), clique = {}'.format(i,j,k,clique(g8,i,j,k)))
                
    print('================ Question 13 ===============')
    g9 = graph_AL.Graph(6,directed=True)
    g9.insert_edge(1,0)
    g9.insert_edge(1,2)
    g9.insert_edge(1,3)    
    g9.insert_edge(0,3)
    g9.insert_edge(2,3)
    g9.insert_edge(3,4)
    g9.insert_edge(2,4)
    g9.display()
    if draw_figs:
        g9.draw()
    print('A topological sort could start with the following vertices:',first_ts(g9)) 
    g9.insert_edge(1,5)
    g9.display()
    if draw_figs:
        g9.draw()
    print('A topological sort could start with the following vertices:',first_ts(g9)) 
    g9.insert_edge(4,1)
    g9.display()
    if draw_figs:
        g9.draw()
    print('A topological sort could start with the following vertices:',first_ts(g9)) 
    
    print('================ Question 14 ===============')
    g8 = graph_AM.Graph(5,directed=True)
    g8.insert_edge(0,1)
    g8.insert_edge(1,2)
    g8.insert_edge(1,3)    
    g8.insert_edge(0,3)
    g8.insert_edge(2,3)
    g8.insert_edge(3,4)
    g8.insert_edge(2,4)
    g8.display()
    if draw_figs:
        g8.draw()
    make_undirected(g8)
    g8.display()
    if draw_figs:
        g8.draw()
    
   
    print('================ Question 15 ===============')
    g9 = graph_AL.Graph(6,directed=True)
    g9.insert_edge(1,0)
    g9.insert_edge(1,2)
    g9.insert_edge(1,3)    
    g9.insert_edge(0,3)
    g9.insert_edge(2,3)
    g9.insert_edge(3,4)
    g9.insert_edge(2,4)
    g9.insert_edge(5,4)
    g9.display()
    if draw_figs:
        g9.draw()
    make_weighted(g9)
    g9.display()
    if draw_figs:
        g9.draw()
    
    print('================ Question 16 ===============')
    g8 = graph_AM.Graph(6,directed=True,weighted=True)
    g8.insert_edge(0,1,3)
    g8.insert_edge(3,2,5)
    g8.insert_edge(1,3,8)    
    g8.insert_edge(5,3,7)
    g8.insert_edge(4,3,2)
    g8.insert_edge(3,4,1)
    g8.insert_edge(2,4,3)
    g8.insert_edge(5,4,5)
    g8.display()
    if draw_figs:
        g8.draw()
    gel = am_to_el(g8)
    gel.display()
    if draw_figs:
        gel.draw()
        
    g8 = graph_AM.Graph(6)
    g8.insert_edge(0,1)
    g8.insert_edge(1,2)
    g8.insert_edge(1,3)    
    g8.insert_edge(0,3)
    g8.insert_edge(2,3)
    g8.insert_edge(3,4)
    g8.insert_edge(2,4)
    g8.insert_edge(5,4)
    g8.display()
    if draw_figs:
        g8.draw()
    gel = am_to_el(g8)
    gel.display()
    if draw_figs:
        gel.draw()
        
    print('================ Question 17 ===============')
    S = [1,2,3,4,6,7]
    for i in range(sum(S)+2):
        print('S=',S,'goal=',i,'number of solutions',subsetsum_count(S,i))
        
    print('================ Question 18 ===============')
    S1 = ['list','btree','hea*']
    S2 = ['lost','heaps','bst*','*eat']
    for s1 in S1:
        for s2 in S2:
            print(s1,s2)
            d = edit_distance_with_wildcard(s1,s2)
            print(d)
        
'''
Program output
================ Question 1 ===============
[2, 0, 1]
[5, 2, 0, 3, 4, 1]
[6, 8, 5, 2, 0, 3, 4, 7, 1]
================ Question 2 ===============
[]
[5]
[7, 8]
[3, 0, 9, 2, 5]
[]
[5]
[7]
[3, 9, 2, 5]
================ Question 3 ===============
[]
[5]
[7, 8]
[3, 0, 9, 2, 5]
[]
[5]
[7, 15]
[3, 3, 12, 14, 19]
================ Question 4 ===============
Original arrays
[[1]
 [2]
 [3]]
[[1 3]
 [2 2]
 [3 5]
 [7 7]]
[[ 1  3  5]
 [ 2  2 12]
 [ 3  3  3]
 [ 7  8  7]
 [ 5  8  7]]
[[1 3 5 6]
 [2 2 2 1]
 [3 3 5 6]
 [7 8 7 6]
 [5 8 7 2]]
Results
[0, 1, 2]
[1, 3]
[2]
[]
================ Question 5 ===============
Original arrays
[[1]
 [2]
 [3]]
[[ 1  3]
 [12  2]
 [ 3  5]
 [ 7  7]]
[[ 1  3  5]
 [ 2  2 12]
 [ 3  3  3]
 [ 7  8  7]
 [ 5  8  7]]
[[ 1 31  5  6]
 [ 2  2  2  1]
 [ 3 13  5  6]
 [ 7 18  7  6]
 [ 5  8  7  2]]
Results
[0, 1, 2]
[0, 2, 3]
[0, 1, 2]
[]
================ Question 6 ===============
depth:0, max:11
depth:1, max:16
depth:2, max:14
depth:3, max:15
depth:4, max:0
depth:5, max:-inf
================ Question 7 ===============
[0, 4, 8, 13, 15]
================ Question 8 ===============
depth:0, max:17
depth:1, max:27
depth:2, max:30
depth:3, max:-inf
================ Question 9 ===============
[6, 11, 17, 23, 27]
================ Question 10 ===============
0 False
1 False
2 False
3 True
4 True
5 True
6 True
7 True
8 True
9 True
10 True
11 True
12 False
13 True
14 False
================ Question 11 ===============
[4, 2, 7, 9, 8, 1]
[4, 2, 7, 9]
[2, 4]
[2302]
[]
================ Question 12 ===============
Graph representation
directed: False, weighted: False
Adjacency matrix:
[[-1  1 -1  1 -1]
 [ 1 -1  1  1 -1]
 [-1  1 -1  1  1]
 [ 1  1  1 -1  1]
 [-1 -1  1  1 -1]]
(u,v,w) = (0,1,2), clique = False
(u,v,w) = (0,1,3), clique = True
(u,v,w) = (0,1,4), clique = False
(u,v,w) = (0,2,3), clique = False
(u,v,w) = (0,2,4), clique = False
(u,v,w) = (0,3,4), clique = False
(u,v,w) = (1,2,3), clique = True
(u,v,w) = (1,2,4), clique = False
(u,v,w) = (1,3,4), clique = False
(u,v,w) = (2,3,4), clique = True
================ Question 13 ===============
Graph representation
directed: True, weighted: False
Adjacency list:
al[0]=[3]
al[1]=[0, 2, 3]
al[2]=[3, 4]
al[3]=[4]
al[4]=[]
al[5]=[]
A topological sort could start with the following vertices: [1, 5]
Graph representation
directed: True, weighted: False
Adjacency list:
al[0]=[3]
al[1]=[0, 2, 3, 5]
al[2]=[3, 4]
al[3]=[4]
al[4]=[]
al[5]=[]
A topological sort could start with the following vertices: [1]
Graph representation
directed: True, weighted: False
Adjacency list:
al[0]=[3]
al[1]=[0, 2, 3, 5]
al[2]=[3, 4]
al[3]=[4]
al[4]=[1]
al[5]=[]
A topological sort could start with the following vertices: []
================ Question 14 ===============
Graph representation
directed: True, weighted: False
Adjacency matrix:
[[-1  1 -1  1 -1]
 [-1 -1  1  1 -1]
 [-1 -1 -1  1  1]
 [-1 -1 -1 -1  1]
 [-1 -1 -1 -1 -1]]
Graph representation
directed: False, weighted: False
Adjacency matrix:
[[-1  1 -1  1 -1]
 [ 1 -1  1  1 -1]
 [-1  1 -1  1  1]
 [ 1  1  1 -1  1]
 [-1 -1  1  1 -1]]
================ Question 15 ===============
Graph representation
directed: True, weighted: False
Adjacency list:
al[0]=[3]
al[1]=[0, 2, 3]
al[2]=[3, 4]
al[3]=[4]
al[4]=[]
al[5]=[4]
Graph representation
directed: True, weighted: True
Adjacency list:
al[0]=[(3,3)]
al[1]=[(0,1), (2,3), (3,4)]
al[2]=[(3,5), (4,6)]
al[3]=[(4,7)]
al[4]=[]
al[5]=[(4,9)]
================ Question 16 ===============
Graph representation
directed: True, weighted: True
Adjacency matrix:
[[-1  3 -1 -1 -1 -1]
 [-1 -1 -1  8 -1 -1]
 [-1 -1 -1 -1  3 -1]
 [-1 -1  5 -1  1 -1]
 [-1 -1 -1  2 -1 -1]
 [-1 -1 -1  7  5 -1]]
Graph representation
directed: True, weighted: True
Edge list:
(0,1,3), (1,3,8), (2,4,3), (3,2,5), (3,4,1), (4,3,2), (5,3,7), (5,4,5)
Graph representation
directed: False, weighted: False
Adjacency matrix:
[[-1  1 -1  1 -1 -1]
 [ 1 -1  1  1 -1 -1]
 [-1  1 -1  1  1 -1]
 [ 1  1  1 -1  1 -1]
 [-1 -1  1  1 -1  1]
 [-1 -1 -1 -1  1 -1]]
Graph representation
directed: False, weighted: False
Edge list:
(0,1), (0,3), (1,2), (1,3), (2,3), (2,4), (3,4), (4,5)
================ Question 17 ===============
S= [1, 2, 3, 4, 6, 7] goal= 0 number of solutions 1
S= [1, 2, 3, 4, 6, 7] goal= 1 number of solutions 1
S= [1, 2, 3, 4, 6, 7] goal= 2 number of solutions 1
S= [1, 2, 3, 4, 6, 7] goal= 3 number of solutions 2
S= [1, 2, 3, 4, 6, 7] goal= 4 number of solutions 2
S= [1, 2, 3, 4, 6, 7] goal= 5 number of solutions 2
S= [1, 2, 3, 4, 6, 7] goal= 6 number of solutions 3
S= [1, 2, 3, 4, 6, 7] goal= 7 number of solutions 4
S= [1, 2, 3, 4, 6, 7] goal= 8 number of solutions 3
S= [1, 2, 3, 4, 6, 7] goal= 9 number of solutions 4
S= [1, 2, 3, 4, 6, 7] goal= 10 number of solutions 5
S= [1, 2, 3, 4, 6, 7] goal= 11 number of solutions 4
S= [1, 2, 3, 4, 6, 7] goal= 12 number of solutions 4
S= [1, 2, 3, 4, 6, 7] goal= 13 number of solutions 5
S= [1, 2, 3, 4, 6, 7] goal= 14 number of solutions 4
S= [1, 2, 3, 4, 6, 7] goal= 15 number of solutions 3
S= [1, 2, 3, 4, 6, 7] goal= 16 number of solutions 4
S= [1, 2, 3, 4, 6, 7] goal= 17 number of solutions 3
S= [1, 2, 3, 4, 6, 7] goal= 18 number of solutions 2
S= [1, 2, 3, 4, 6, 7] goal= 19 number of solutions 2
S= [1, 2, 3, 4, 6, 7] goal= 20 number of solutions 2
S= [1, 2, 3, 4, 6, 7] goal= 21 number of solutions 1
S= [1, 2, 3, 4, 6, 7] goal= 22 number of solutions 1
S= [1, 2, 3, 4, 6, 7] goal= 23 number of solutions 1
S= [1, 2, 3, 4, 6, 7] goal= 24 number of solutions 0
================ Question 18 ===============
list lost
[[1 2 2 3 4]
 [2 1 1 2 3]
 [2 1 0 1 2]
 [3 2 1 0 1]
 [4 3 2 1 0]]
list heaps
[[5 4 3 3 3 4]
 [5 4 3 2 2 3]
 [5 4 3 2 1 2]
 [5 4 3 2 1 1]
 [5 4 3 2 1 0]]
list bst*
[[3 3 3 3 4]
 [2 2 2 2 3]
 [2 1 1 1 2]
 [3 2 1 0 1]
 [4 3 2 1 0]]
list *eat
[[2 3 3 3 4]
 [2 2 2 2 3]
 [2 2 1 1 2]
 [3 2 1 0 1]
 [4 3 2 1 0]]
btree lost
[[5 5 4 4 5]
 [4 4 4 3 4]
 [4 3 3 3 3]
 [4 3 2 2 2]
 [4 3 2 1 1]
 [4 3 2 1 0]]
btree heaps
[[5 5 5 5 5 5]
 [5 4 4 4 4 4]
 [4 4 3 3 3 3]
 [4 3 3 2 2 2]
 [4 3 3 2 1 1]
 [5 4 3 2 1 0]]
btree bst*
[[3 3 3 4 5]
 [3 3 2 3 4]
 [3 2 2 2 3]
 [3 2 1 1 2]
 [3 2 1 0 1]
 [4 3 2 1 0]]
btree *eat
[[4 5 4 4 5]
 [3 4 4 3 4]
 [2 3 3 3 3]
 [2 2 2 2 2]
 [3 2 2 1 1]
 [4 3 2 1 0]]
hea* lost
[[3 3 3 3 4]
 [3 2 2 2 3]
 [3 2 1 1 2]
 [3 2 1 0 1]
 [4 3 2 1 0]]
hea* heaps
[[1 2 3 3 3 4]
 [2 1 2 2 2 3]
 [3 2 1 1 1 2]
 [4 3 2 1 0 1]
 [5 4 3 2 1 0]]
hea* bst*
[[3 3 3 3 4]
 [3 2 2 2 3]
 [3 2 1 1 2]
 [3 2 1 0 1]
 [4 3 2 1 0]]
hea* *eat
[[0 1 2 3 4]
 [1 0 1 2 3]
 [2 1 0 1 2]
 [3 2 1 0 1]
 [4 3 2 1 0]]   

'''