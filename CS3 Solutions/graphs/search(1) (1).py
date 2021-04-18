import numpy as np
import matplotlib.pyplot as plt
import math
import graph_AL as graph
import min_heap

def get_path(prev,v):
    if prev[v]<0:
        return [v]
    return get_path(prev,prev[v])+[v]

def print_paths(prev):
    for v in range(len(prev)):
        print('Path to',v,':',get_path(prev,v))
        
def dfs(G,source,visited,prev,trace=False):
    visited[source] = True
    if trace:
        print('source=',source)
        print('visited=',visited)
        print('prev=',prev)
    for edge in G.al[source]:
        if not visited[edge.dest]:
            prev[edge.dest] = source
            dfs(G,edge.dest,visited,prev,trace=True)
            
    
def dfs_stack(G,source=0,trace=False):
    visited = [False for i in range(len(G.al))]
    prev = [-1 for i in range(len(G.al))]
    visited[source] = True
    S = [source]
    while len(S)>0:
        v = S.pop()
        visited[v] = True
        for i in range(len(G.al[v])-1,-1,-1):
            u = G.al[v][i].dest
            if not visited[u]:
                prev[u] = v
                S.append(u)
        if trace:
            print('v=',v)
            print('visited=',visited)
            print('prev=',prev)
            print('S=',S)
    return prev

def bfs(G,source=0,trace=False):
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
        if trace:
            print('v=',v)
            print('visited=',visited)
            print('prev=',prev)
            print('Q=',Q)
    return prev

def dijkstra(G,source=0,trace=False):
    known = [False for i in range(len(G.al))]
    prev = [-1 for i in range(len(G.al))]
    dist =[math.inf for i in range(len(G.al))]
    dist_heap = min_heap.MinHeap()
    dist[source] = 0
    dist_heap.insert(min_heap.HeapRecord(dist[source],source))
    while len(dist_heap.heap)>0:
        heap_node = dist_heap.extractMin()
        v = heap_node.data
        if not known[v]:
            known[v] = True
            for edge in G.al[v]:
                u = edge.dest
                if not known[u]:
                    w = edge.weight
                    if dist[v]+w < dist[u]:
                        prev[u] = v
                        dist[u] = dist[v]+w
                        dist_heap.insert(min_heap.HeapRecord(dist[u],u))
            if trace:
                print('v=',v)
                print('known=',known)
                print('prev=',prev)
                print('dist=',dist)               
    return prev, dist


if __name__ == "__main__":   
    plt.close("all")   
    
    G =graph.Graph(6,directed = True)
    G.insert_edge(0,1)
    G.insert_edge(0,2)
    G.insert_edge(1,4)
    G.insert_edge(2,1)
    G.insert_edge(3,2)
    G.insert_edge(4,3)
    G.insert_edge(4,5)
    G.display()
    G.draw()
    prev =  bfs(G,trace=True)
    
    print_paths(prev)
        
    prev =  dfs_stack(G,trace=True)
    
    print_paths(prev)
    
    G =graph.Graph(9,directed = True)
    G.insert_edge(0,1)
    G.insert_edge(0,4)
    G.insert_edge(1,2)
    G.insert_edge(1,5)
    G.insert_edge(2,3)
    G.insert_edge(4,1)
    G.insert_edge(4,5)
    G.insert_edge(4,7)
    G.insert_edge(5,2)
    G.insert_edge(5,6)
    G.insert_edge(5,8)
    G.insert_edge(6,2)
    G.insert_edge(6,3)
    G.insert_edge(7,5)
    G.insert_edge(7,8)
    G.insert_edge(8,6)
    
    prev =  bfs(G,trace=True)
    
    print_paths(prev)
        
    prev =  dfs_stack(G,trace=True)
    
    print_paths(prev)
     
    visited = [False for i in range(len(G.al))]
    prev = [-1 for i in range(len(G.al))]
    dfs(G,0,visited,prev,trace=True)
    print_paths(prev)
    
    G =graph.Graph(5,directed = True,weighted =True)
    G.insert_edge(0,1,4)
    G.insert_edge(0,2,7)
    G.insert_edge(1,2,2)
    G.insert_edge(2,3,1)
    G.insert_edge(2,4,8)    
    G.insert_edge(3,4,5)
    G.insert_edge(4,1,4)
    G.display()
    G.draw()
    
    prev, dist = dijkstra(G,trace=True)
    
    G =graph.Graph(9,directed = True,weighted =True)
    G.insert_edge(0,1,4)
    G.insert_edge(0,4,3)
    G.insert_edge(1,2,9)
    G.insert_edge(1,5,2)
    G.insert_edge(2,3,5)
    G.insert_edge(4,1,2)
    G.insert_edge(4,5,4)
    G.insert_edge(4,7,1)
    G.insert_edge(5,2,3)
    G.insert_edge(5,6,7)
    G.insert_edge(5,8,2)
    G.insert_edge(6,2,4)
    G.insert_edge(6,3,3)
    G.insert_edge(7,5,1)
    G.insert_edge(7,8,2)
    
    G.insert_edge(8,6,6)    
    
    G.display()
    G.draw()
    
    prev, dist = dijkstra(G,trace=True)
    
    