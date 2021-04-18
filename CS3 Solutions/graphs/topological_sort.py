import numpy as np
import matplotlib.pyplot as plt
import graph_AL as graph

def in_degrees(G):
    L = [0 for i in range(len(G.al))]
    for vert in G.al:
        for edge in vert:
            L[edge.dest] +=1
    return L

def topological_sort(G,trace=False):
    in_deg = in_degrees(G)
    ts = []
    Q = [i for i in range(len(in_deg)) if in_deg[i]==0]
    # Q=[]
    # for i in range(len(in_deg)):
    #     if in_deg[i]==0:
    #         Q.append(i)
    while len(Q)>0:
        v = Q.pop(0)
        ts.append(v)
        for edge in G.al[v]:
            u = edge.dest
            in_deg[u] -= 1
            if in_deg[u] == 0:
                Q.append(u)
        if trace:
            print('v=',v)
            print('Q=',Q)
            print('in_deg=',in_deg)
    if len(ts) == len(G.al):
        return ts
    return None
                
if __name__ == "__main__":   
    plt.close("all")  
    
    print('=== Graph 1 ===')
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
    G.draw(' ')
    s = topological_sort(G,trace=True)
    print('Topological sort:',s)
   
    print('===Graph 2 ===')
    G =graph.Graph(9,directed = True)
    G.insert_edge(0,1)
    G.insert_edge(0,4)
    G.insert_edge(1,2)
    G.insert_edge(3,2)
    G.insert_edge(4,1)
    G.insert_edge(4,5)
    G.insert_edge(4,7)
    G.insert_edge(5,1)
    G.insert_edge(5,2)
    G.insert_edge(5,6)
    G.insert_edge(5,8)
    G.insert_edge(6,2)
    G.insert_edge(6,3)
    G.insert_edge(7,5)
    G.insert_edge(7,8)
    G.insert_edge(8,6)
    G.draw(' ')
    s = topological_sort(G)
    print('Topological sort:',s)
   
