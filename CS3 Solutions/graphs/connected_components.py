import numpy as np
import matplotlib.pyplot as plt
import graph_AL as graph
import dsf

def connected_components(G,trace=False):
    # Returns the disjoint set forest representing the connected components of G
    S = dsf.DSF(len(G.al))  
    for v in range(len(G.al)):
        for edge in G.al[v]:
            if v<edge.dest:
                S.union(v,edge.dest)
                if trace:
                    print('last edge: ({},{})'.format(v,edge.dest))
                    print('dsf:',S.parent)
    return S

if __name__ == "__main__":   
    plt.close("all")   
    
    G =graph.Graph(8)
    G.insert_edge(0,2)
    G.insert_edge(0,3)
    G.insert_edge(1,3)
    G.insert_edge(1,4)
    G.insert_edge(2,3)
    G.insert_edge(3,4)
    G.insert_edge(5,6)
    
    G.display()
    G.draw('Original graph')

    S = connected_components(G,trace=True)
    s = S.set_list()
    print('Disjoint set forest:',S.parent)
    print('Number of connected components:',len(s))
    print('Connected components:',s)
    S.draw()
    
    G =graph.Graph(8)
    G.insert_edge(0,2)
    G.insert_edge(0,3)
    G.insert_edge(1,5)
    G.insert_edge(2,3)
    G.insert_edge(3,4)
    G.insert_edge(5,6)
    
    G.display()
    G.draw('Original graph')
    
    S = connected_components(G,trace=True)
    s = S.set_list()
    print('Disjoint set forest:',S.parent)
    print('Number of connected components:',len(s))
    print('Connected components:',s)
    S.draw()
    
    
