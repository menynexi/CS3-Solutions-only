import numpy as np
import matplotlib.pyplot as plt
import math
import graph_EL as graph

#Question 1
def num_vertices(G):
    return G.vertices

#Question 2
def count_edges(G):
    return len(G.el)
    
#Question 3
def highest_weight_edge(G):
    biggest = [0,0,-math.inf]
    for e in G.el:
        if biggest[2] < e.weight:
                biggest = [e.source, e.dest, e.weight]
    return biggest

#Question 4
def circle_graph(n):
    g = graph.Graph(n, directed = True)
    for i in range(n):
        g.el.append(graph.Edge(i,(i+1)%n))
    return g

#Question 5
def out_degrees(G):
    L = [0 for i in range(G.vertices)]
    for e in G.el:
        L[e.source]+=1
    if not G.directed:
        for e in G.el:
            L[e.dest]+=1
    return L

#question 6
def in_degrees(G):
    L = [0 for i in range(G.vertices)]
    for e in G.el:
        L[e.dest]+=1
    if not G.directed:
        for e in G.el:
            L[e.source]+=1
    return L


if __name__ == "__main__":   
    plt.close("all")   
    g_uduw =graph.Graph(5)
    g_uduw.insert_edge(0,1)
    g_uduw.insert_edge(0,2)
    g_uduw.insert_edge(1,2)
    g_uduw.insert_edge(2,3)
    g_uduw.insert_edge(3,4)
    g_uduw.insert_edge(4,1)
    g_uduw.display()
    g_uduw.draw()
    
    g_duw = graph.Graph(5,directed = True)
    g_duw.insert_edge(0,1)
    g_duw.insert_edge(0,2)
    g_duw.insert_edge(1,2)
    g_duw.insert_edge(2,3)
    g_duw.insert_edge(3,4)
    g_duw.insert_edge(4,1)
    g_duw.display()
    g_duw.draw()
    
    g_udw = graph.Graph(5, weighted=True)
    g_udw.insert_edge(0,1,4)
    g_udw.insert_edge(0,2,3)
    g_udw.insert_edge(1,2,2)
    g_udw.insert_edge(2,3,1)
    g_udw.insert_edge(3,4,5)
    g_udw.insert_edge(4,1,4)
    g_udw.display()
    g_udw.draw()
    
    g_dw = graph.Graph(5,directed = True, weighted=True)
    g_dw.insert_edge(0,1,4)
    g_dw.insert_edge(0,2,3)
    g_dw.insert_edge(1,2,2)
    g_dw.insert_edge(2,3,1)
    g_dw.insert_edge(3,4,5)
    g_dw.insert_edge(4,1,4)
    g_dw.display()
    g_dw.draw()
    
    print('Question 1')
    print("Vertices: ",num_vertices(g_uduw))  # 5
    print("Vertices: ",num_vertices(g_duw))   # 5
    print("Vertices: ",num_vertices(g_udw))   # 5
    print("Vertices: ",num_vertices(g_dw))    # 5
    
    print('Question 2')
    print("Edges: ",count_edges(g_uduw))  # 6
    print("Edges: ",count_edges(g_duw))   # 6
    print("Edges: ",count_edges(g_udw))   # 6
    print("Edges: ",count_edges(g_dw))    # 6
    
    print('Question 3')
    print("Highest weight edge: ",highest_weight_edge(g_uduw))  # [0, 1, 1]
    print("Highest weight edge: ",highest_weight_edge(g_duw))   # [0, 1, 1]
    print("Highest weight edge: ",highest_weight_edge(g_udw))   # [3, 4, 5]
    print("Highest weight edge: ",highest_weight_edge(g_dw))    # [3, 4, 5]
    
    print('Question 4')
    g_circ = circle_graph(5)
    g_circ.display()
    g_circ.draw('Circle graph')
    
    print('Question 5')
    print("Out degrees: ",out_degrees(g_uduw))  # [2, 3, 3, 2, 2]
    print("Out degrees: ",out_degrees(g_duw))   # [2, 1, 1, 1, 1]
    print("Out degrees: ",out_degrees(g_udw))   # [2, 3, 3, 2, 2]
    print("Out degrees: ",out_degrees(g_dw))    # [2, 1, 1, 1, 1]
    
    print('Question 6')
    print("In degrees: ",in_degrees(g_uduw))  # [2, 3, 3, 2, 2]
    print("In degrees: ",in_degrees(g_duw))   # [0, 2, 2, 1, 1]
    print("In degrees: ",in_degrees(g_udw))   # [2, 3, 3, 2, 2]
    print("In degrees: ",in_degrees(g_dw))    # [0, 2, 2, 1, 1]
