import numpy as np
import matplotlib.pyplot as plt
import graph_AL as graph
import dsf
import min_heap
from scipy.interpolate import interp1d

def draw(ax,g,color):
    scale = 30
    for i in range(len(g.al)):
        for edge in g.al[i]:
            d,w = edge.dest, edge.weight
            if d>i:
                x = np.linspace(i*scale,d*scale)
                x0 = np.linspace(i*scale,d*scale,num=5)
                diff = np.abs(d-i)
                if diff == 1:
                    y0 = [0,0,0,0,0]
                else:
                    y0 = [0,-6*diff,-8*diff,-6*diff,0]
                f = interp1d(x0, y0, kind='cubic')
                y = f(x)
                s = np.sign(i-d)
                ax.plot(x,s*y,linewidth=1,color=color)
                if g.weighted:
                    xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                    yd = [y0[2]-1,y0[2],y0[2]+1]
                    yd = [y*s for y in yd]
                    ax.text(xd[2]-s*2,yd[2]+3*s, str(w), size=12,color=color, ha="center", va="center")
        ax.plot([i*scale,i*scale],[0,0],linewidth=1,color='k')        
        ax.text(i*scale,0, str(i), size=20,ha="center", va="center",bbox=dict(facecolor='w',boxstyle="circle"))
   
def draw_over(g1,g2,title=''):
    fig, ax = plt.subplots()
    draw(ax,g1,'k')
    draw(ax,g2,'r')
    ax.axis('off') 
    ax.set_aspect(1.0)
    fig.suptitle(title, fontsize=16)                    
                        
def kruskal(G,trace=False):
    weight_heap = min_heap.MinHeap()
    S = dsf.DSF(len(G.al))
    for v in range(len(G.al)):
        for edge in G.al[v]:
            if v<edge.dest:
                weight_heap.insert(min_heap.HeapRecord(edge.weight,[v,edge.dest,edge.weight]))
    mst = graph.Graph(len(G.al),weighted=True)
    count = 0
    while count<len(G.al)-1 and len(weight_heap.heap)>0:
        next_edge = weight_heap.extractMin().data
        if S.union(next_edge[0],next_edge[1])==1:
            mst.insert_edge(next_edge[0],next_edge[1],next_edge[2])
            count+=1
            if trace:
                draw_over(G,mst,'Kruskal '+str(count))
                print(next_edge,'added to mst')
        else:
            if trace:
                print(next_edge,'rejected')
        
    if count == len(G.al)-1:
        return mst
    print('Graph has no minimum spanning tree')
    return None

def prim(G,origin=0, trace=False):
    weight_heap = min_heap.MinHeap()
    connected = set([origin])
    for edge in G.al[origin]:
        weight_heap.insert(min_heap.HeapRecord(edge.weight,[origin,edge.dest,edge.weight]))
    mst = graph.Graph(len(G.al),weighted=True)
    count = 0
    while count<len(G.al)-1 and len(weight_heap.heap)>0:
        next_edge = weight_heap.extractMin().data
        if next_edge[0] not in connected:
            new_vertex = next_edge[0]
        elif next_edge[1] not in connected:
            new_vertex = next_edge[1]  
        else:
            continue
        mst.insert_edge(next_edge[0],next_edge[1],next_edge[2])
        connected.add(new_vertex)
        count+=1
        if trace:
            draw_over(G,mst,'Prim '+str(count))
            print(next_edge,'added to mst')
        for edge in G.al[new_vertex]:
            if edge.dest not in connected:
                weight_heap.insert(min_heap.HeapRecord(edge.weight,[new_vertex,edge.dest,edge.weight]))    
    if count == len(G.al)-1:
        return mst
    print('Graph has no minimum spanning tree')
    return None

if __name__ == "__main__":   
    plt.close("all")   
    
    g = graph.Graph(7,weighted=True)
    g.insert_edge(0,1,8)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.insert_edge(4,6,9)
    g.insert_edge(5,6,10)
    g.insert_edge(4,5,6)
    g.insert_edge(3,6,7)
    g.display()
    g.draw('Original graph')
    
    # print('Kruskal')
    # mst = kruskal(g,trace=True)
    
    
    # if mst!=None:
    #     mst.draw('Kruskal')
    #     mst.display()
        
    print('Prim')
    mst = prim(g,origin=6,trace=True)
    if mst!=None:
        mst.draw('Prim')
        mst.display()
'''
Program output:        
Graph representation
directed: False, weighted: True
Adjacency list:
al[0]=[(1,8), (2,3)]
al[1]=[(0,8), (2,2), (4,4)]
al[2]=[(0,3), (1,2), (3,1)]
al[3]=[(2,1), (4,5), (6,7)]
al[4]=[(3,5), (1,4), (6,9), (5,6)]
al[5]=[(6,10), (4,6)]
al[6]=[(4,9), (5,10), (3,7)]
Kruskal
[2, 3, 1] added to mst
[1, 2, 2] added to mst
[0, 2, 3] added to mst
[1, 4, 4] added to mst
[3, 4, 5] rejected
[4, 5, 6] added to mst
[3, 6, 7] added to mst
Graph representation
directed: False, weighted: True
Adjacency list:
al[0]=[(2,3)]
al[1]=[(2,2), (4,4)]
al[2]=[(3,1), (1,2), (0,3)]
al[3]=[(2,1), (6,7)]
al[4]=[(1,4), (5,6)]
al[5]=[(4,6)]
al[6]=[(3,7)]
Prim
[0, 2, 3] added to mst
[2, 3, 1] added to mst
[2, 1, 2] added to mst
[1, 4, 4] added to mst
[4, 5, 6] added to mst
[3, 6, 7] added to mst
Graph representation
directed: False, weighted: True
Adjacency list:
al[0]=[(2,3)]
al[1]=[(2,2), (4,4)]
al[2]=[(0,3), (3,1), (1,2)]
al[3]=[(2,1), (6,7)]
al[4]=[(1,4), (5,6)]
al[5]=[(4,6)]
al[6]=[(3,7)]
'''