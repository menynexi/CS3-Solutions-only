# Code to implement basic min heap operations
# Programmed by Olac Fuentes
# Last modified July 5, 2020

import matplotlib.pyplot as plt
import numpy as np

class HeapRecord:
    def __init__(self,key, data=''):  
        self.key = key
        self.data = data

class MinHeap:
    def __init__(self):  
        self.heap = []

    def insert(self,rec):
        # Add record to head. If rec is an int, it creates a HeapRecord
        if type(rec)==int:
            rec = HeapRecord(rec)
        self.heap.append(rec) # Add new item to end of heap
        i = len(self.heap)-1
        while i>0 and rec.key < self.heap[self.parent(i)].key:
            self.heap[i] = self.heap[self.parent(i)] 
            i = self.parent(i)
        self.heap[i] = rec
        
    def extractMin(self):
        assert len(self.heap)>0 # Raise error if trying to extractMin from empty heap
        if len(self.heap) == 1:
            return self.heap.pop() # Return and remove root; heap is now empty
        root = self.heap[0]
        self.heap[0] = self.heap.pop() # Move last element from heap to root, reduce heap size
        i = 0
        while True:
            smallest = i
            for k in [self.leftChild(i),self.rightChild(i)]:
                if k < len(self.heap) and self.heap[k].key < self.heap[smallest].key:
                    smallest = k
            if smallest == i: # Parent is not smaller than either of its children
                 return root
            self.heap[i],self.heap[smallest] = self.heap[smallest],self.heap[i] # Swap parent with smaller child
            i = smallest
            
    def parent(self,i):
        return (i-1)//2
    
    def leftChild(self,i):
        return 2*i + 1
    
    def rightChild(self,i):
        return 2*i + 2
    
    def draw(self):
        if len(self.heap)>0:
            fig, ax = plt.subplots()
            self.dh(0, 0, 0, 100, 50, ax)
            ax.axis('off') 
            ax.set_aspect(1.0)
        
    def dh(self, i, x, y, dx, dy, ax):
        if self.leftChild(i) < len(self.heap):
            p=np.array([[x,y], [x-dx,y-dy]])
            ax.plot(p[:,0],p[:,1],linewidth=1,color='k')
            self.dh(self.leftChild(i), x-dx, y-dy, dx/2, dy, ax)
        if self.rightChild(i) < len(self.heap): 
            p=np.array([[x,y], [x+dx,y-dy]])
            ax.plot(p[:,0],p[:,1],linewidth=1,color='k')
            self.dh(self.rightChild(i), x+dx, y-dy, dx/2, dy, ax)
        ax.text(x,y, str(self.heap[i].key), size=20,
             ha="center", va="center",
             bbox=dict(facecolor='w',boxstyle="circle"))
        #ax.text(x-4,y-32, str(i), size=15,color='r')

def heapsort(L):
    H = MinHeap()
    Ls = []
    for i in L:
        H.insert(i)
    for j in range(len(L)):
        Ls.append(H.extractMin().key)
    return Ls


if __name__ == "__main__":           
    plt.close("all")     
    H = MinHeap()
    A = [15,13,9,8,4,7,16,10,17,1]
    for a in A:
        H.insert(a)
        print('Inserted',a,'heap size:',len(H.heap))
        H.draw() 
    
    for i in range(len(A)):
        m = H.extractMin()
        print('Extracted',m.key,'heap size:',len(H.heap))
        H.draw() 
       
    print(heapsort(A))