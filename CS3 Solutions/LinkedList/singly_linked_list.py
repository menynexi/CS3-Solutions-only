# Program to implement and display singly-linked lists
# Programmed by Olac Fuentes
# Last modified June 19, 2020

import matplotlib.pyplot as plt
import numpy as np 

class ListNode:
    # Constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class List:
    # Constructor
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        t = self.head
        print('[',end ='')
        while t is not None:
            print(t.data,end='')
            t = t.next
            if t!= None:
                print(', ',end='')
        print(']')

    def append(self,x):
        if self.head is None: #List is empty
            self.head = ListNode(x)
            self.tail = self.head
        else:
            self.tail.next = ListNode(x)
            self.tail = self.tail.next

    def extend(self,python_list):
        for d in python_list:
            self.append(d)

    def _rectangle(self,x0,y0,dx,dy):
        # Returns the coordinates of the corners of a rectangle
        # with bottom-left corner (x0,y0), dx width and dy height
        x = [x0,x0+dx,x0+dx,x0,x0]
        y = [y0,y0,y0+dy,y0+dy,y0]
        return x,y

    def draw(self,figure_name=' ',text_size=10):
        # Drawing function, don't worry about fully understanding it
        # Assumes the list contains no loops
        larger_text_size=text_size*3//2
        fig, ax = plt.subplots()
        x, y = self._rectangle(0,-5,20,30)
        ax.plot(x,y,linewidth=2,color='r')
        ax.plot([0,20],[10,10],linewidth=1,color='k')
        ax.text(-2,17, 'head', size=text_size,ha="right", va="center")
        ax.text(-2,1, 'tail', size=text_size,ha="right", va="center")
        t = self.head
        x0 = 40
        while t !=None:
            x, y = self._rectangle(x0,0,30,20)
            ax.plot(x,y,linewidth=2,color='b')
            ax.plot([x0+15,x0+15],[0,20],linewidth=1,color='k')
            ax.text(x0+7,10, str(t.data), size=text_size,ha="center", va="center")
            #ax.text(x0+5,25, 'data', size=text_size,ha="center", va="center")
            #ax.text(x0+25,25, 'next', size=text_size,ha="center", va="center")
            if t.next == None:
                ax.text(x0+22,10, '/', size=text_size,ha="center", va="center")
            else:
                ax.plot([x0+22,x0+40],[10,10],linewidth=1,color='k')
                ax.plot([x0+37,x0+40,x0+37],[7,10,13],linewidth=1,color='k')
            t = t.next
            x0 = x0+40
        if self.head == None:
            ax.text(12,17, '/', size=text_size,ha="center", va="center")
        else:
            ax.plot([10,40],[17,17],linewidth=1,color='k')
            ax.plot([37,40,37],[14,17,20],linewidth=1,color='k')

        if self.tail == None:
            ax.text(12,1, '/', size=text_size,ha="center", va="center")
        else:
            xt = 40
            t = self.head
            while t!= self.tail:
                t = t.next
                xt+=40
            ax.plot([10,10,xt+15,xt+15],[1,-10,-10,0],linewidth=1,color='k')
            ax.plot([xt+12,xt+15,xt+18],[-3,0,-3],linewidth=1,color='k')

        ax.set_title(figure_name)
        ax.set_aspect(1.0)
        ax.axis('off')
        fig.set_size_inches(1.2*(x0+200)/fig.get_dpi(),100/fig.get_dpi())
        plt.show()

if __name__ == "__main__":
        
    plt.close('all')
    
    L1 = List()
    L1.draw('Empty list')
    L1.extend(list(np.random.permutation(10)))
    L1.draw('Unsorted list')
    L1 = List()
    L1.extend(list(np.arange(10)))
    L1.draw('Sorted list')
    L1.tail = L1.head.next.next
    L1.draw('Bad list!')
    L1.tail = None
    L1.draw('Another bad list!')
    
    L =List()
   
    for i in range(4):
        L.head = ListNode(i,L.head)
        if L.tail == None:
            L.tail = L.head
    L.draw()
   
    L.print()
   
    L= List()
    
    L.extend([9,3,6,2])
    L.draw()
    L.head = L.head.next
    L.draw()