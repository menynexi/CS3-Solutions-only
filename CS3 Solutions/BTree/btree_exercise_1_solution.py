import matplotlib.pyplot as plt
import numpy as np
import btree

def print_data(T):
    if type(T)==btree.BTree:
        T=T.root
    if T.is_leaf:
        for d in T.data:
            print(d,end=' ')
    else:
        for i in range(len(T.data)):
            print_data(T.child[0])
            print(T.data[i],end=' ')
        print_data(T.child[-1])



def smallest(T):
    t = T.root
    while not t.is_leaf:
        t = t.child[0]
    return t.data[0]



















def largest(T):
    t = T.root
    while not t.is_leaf:
        t = t.child[-1]
    return t.data[-1]
















def numNodes(T):
    if type(T)==btree.BTree:
        T=T.root
    count = 1
    if not T.is_leaf:
        for c in T.child:
            count+= numNodes(c)
    return count












def numItems(T):
    if type(T)==btree.BTree:
        T=T.root
    count = len(T.data)
    if not T.is_leaf:
        for c in T.child:
            count+= numItems(c)
    return count











if __name__ == "__main__":
    plt.close('all')
    T = btree.BTree()

    nums = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
  
    for num in nums:
        T.insert(num)
    T.draw()

    print_data(T)
    print()

    print(smallest(T))  
    print(largest(T))   
    print(numNodes(T))  
    print(numItems(T))  

'''
Program output:
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 
1
30
9
30
'''