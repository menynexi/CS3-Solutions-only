# Code to implement basic binary search tree operations
# Programmed by Olac Fuentes
# Last modified June 24, 2020

import matplotlib.pyplot as plt
import numpy as np

class BSTNode:

    def __init__(self, data,  left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self,newdata):
        if self.data > newdata:
            if self.left == None:
                self.left = BSTNode(newdata)
            else:
                self.left.insert(newdata)
        else:
            if self.right == None:
                self.right = BSTNode(newdata)
            else:
                self.right.insert(newdata)

    def inOrder(self):
        if self.left !=None:
            self.left.inOrder()
        print(self.data,end=' ')
        if self.right !=None:
            self.right.inOrder()

    def draw(self, ax, x0, y0, delta_x, delta_y):
        delta_x = max([20,delta_x])
        if self.left is not None:
            ax.plot([x0-delta_x,x0],[y0-delta_y,y0],linewidth=1,color='k')
            self.left.draw(ax, x0-delta_x, y0-delta_y, delta_x/2, delta_y)
        if self.right is not None:
            ax.plot([x0+delta_x,x0],[y0-delta_y,y0],linewidth=1,color='k')
            self.right.draw(ax, x0+delta_x, y0-delta_y, delta_x/2, delta_y)
        ax.text(x0,y0, str(self.data), size=14,ha="center", va="center",
            bbox=dict(facecolor='w',boxstyle="circle"))

    def find(self,data):
        if self.data == data:
            return self
        if self.data > data:
            child = self.left
        else:
            child = self.right
        if child == None:
            return None
        else:
            return child.find(data)

class BST:

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self,newdata):
        if self.root == None:
            self.root = BSTNode(newdata)
        else:
            self.root.insert(newdata)
        self.size += 1

    def inOrder(self):
        if self.root != None:
            self.root.inOrder()
            print()
        else:
            print('Tree is empty')

    def draw(self):
        if self.root != None:
            fig, ax = plt.subplots()
            self.root.draw(ax, 0, 0, 1000, 120)
            ax.axis('off')
            plt.show()

    def find(self,data):
        if self.root == None:
            return None
        return self.root.find(data)

            
if __name__ == "__main__":
    plt.close('all')
    A =[11, 6, 7, 16, 2, 4, 14, 8, 15, 1, 13, 0]
    T = BST()

    for a in A:
        T.insert(a)

    T.inOrder()
    
    T.draw()
    print('Tree size:',T.size)
    
  

