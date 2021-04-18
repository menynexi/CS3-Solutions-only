# Edge list representation of graphs
# Programmed by Olac Fuentes
# Last modified July 13, 2020

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d
import graph_AL

class Edge:
    def __init__(self, source, dest, weight=1):
        self.source = source
        self.dest = dest
        self.weight = weight
        
class Graph:
    def __init__(self,  vertices, weighted=False, directed = False):
        self.vertices = vertices
        self.el = []
        self.weighted = weighted
        self.directed = directed
        
    def insert_edge(self,source,dest,weight=1):
        if source >= self.vertices or dest>=self.vertices or source <0 or dest<0:
            print('Error, vertex number out of range')
            return False
        elif weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
            return False
        else:
            self.el.append(Edge(source,dest,weight))
            return True
        
    def delete_edge(self,source,dest):
        i = 0
        for edge in self.el:
            if edge.source == source and edge.dest == dest:
                self.el.pop(i)
                return True
            i+=1    
        return False
        
    def display(self):
        print('Graph representation')
        print('directed: {}, weighted: {}'.format(self.directed,self.weighted))
        print('Edge list:')
        p=''
        if self.weighted:
            for edge in self.el:
                print(p+'({},{},{})'.format(edge.source,edge.dest,edge.weight),end='')
                p=', '
        else:
            for edge in self.el:
                print(p+'({},{})'.format(edge.source,edge.dest),end='')
                p=', '
        print()
     
    def draw(self,title=''):
        self.as_AL().draw(title)
            
    def as_AL(self):
        g_al = graph_AL.Graph(vertices = self.vertices, weighted = self.weighted, directed = self.directed)
        for edge in self.el:
            g_al.insert_edge(edge.source,edge.dest,edge.weight)
        return g_al
    
if __name__ == "__main__":   
    plt.close("all")   
    g = Graph(5)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
    g.draw()
    
    g.delete_edge(1,2)
    g.display()
    g.draw()
    
    g = Graph(5,directed = True)
    g.insert_edge(0,1)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,0)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    
    g = Graph(5,weighted=True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    
    g = Graph(5,weighted=True,directed = True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    
    
