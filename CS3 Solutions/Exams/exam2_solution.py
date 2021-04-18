import matplotlib.pyplot as plt
import numpy as np
import min_heap
import bst
import btree
import hash_table_chain as htc
import math

def print_data(T):
    if type(T)==btree.BTree:
        print_data(T.root)
        print()
        return
    if T.is_leaf:
        for d in T.data:
            print(d,end=' ')
    else:
        for i in range(len(T.data)):
            print_data(T.child[i])
            print(T.data[i],end=' ')
        print_data(T.child[-1])

def decrease_min(t):
    t = t.root
    while t.left!=None:
        t=t.left
    t.data-=1

def increase_max(T):
    t = T.root
    while not t.is_leaf:
        t = t.child[-1]
    t.data[-1]+=1

def remove_same_hash(H,k):
    H.bucket[H.h(k)] =[]
    
def sibling(H,k):
    s = k + 2*(k%2) - 1 
    if k<1 or s>=len(H.heap) or k>=len(H.heap):
        return None
    return H.heap[s].key
    
def one_child_nodes(t):
    if type(t) == bst.BST:
        t=t.root
    if t==None:
        return 0
    count = one_child_nodes(t.left)+one_child_nodes(t.right)
    children = int(t.left!=None) + int(t.right!=None)
    if children ==1:
        count+=1
    return count

def data_at_depth_d_or_less(T,d):
    if type(T)==btree.BTree:
        T=T.root
    if d==0 or T.is_leaf:
        return T.data
    L = []
    for i in range(len(T.data)):
        L = L+data_at_depth_d_or_less(T.child[i],d-1)
        L.append(T.data[i])
    return L+data_at_depth_d_or_less(T.child[-1],d-1)
       
def missing_pair(L):
    H = htc.HashTableChain(len(L))
    for i in L:
        c = H.retrieve(i)
        if c==None:
            H.insert(i)
        else:
            H.delete(i)    
    for b in H.bucket:
        if len(b)>0:
            return b[0].key
    return None
    
def unique_min(H):
    if len(H.heap)>1 and H.heap[0].key==H.heap[1].key:
        return False
    if len(H.heap)>2 and H.heap[0].key==H.heap[2].key:
        return False
    return True    
    
if __name__ == "__main__":
    plt.close('all')
    
    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 12]
    TA = bst.BST()
    for a in A:
        TA.insert(a)
    TA.draw()
    
    B =[ 6, 10, 7, 16, 17, 18, 14, 8, 15]
    TB = bst.BST()
    for b in B:
        TB.insert(b)
    TB.draw()
    
    print('Question 1')
    
    TA.inOrder()
    decrease_min(TA)
    TA.inOrder()
    TA.draw()
    TB.inOrder()
    decrease_min(TB)
    TB.inOrder()
    TB.draw()
   
    print('Question 2')
    
    nums = [6, 3, 23,16, 11, 25, 7,21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
    T = btree.BTree()
    for num in nums:
        T.insert(num)
    T.draw()
    print_data(T)
    increase_max(T)
    T.draw()
    print_data(T)
    
    print('Question 3')
    
    L = [2,4,6,11,13,3,1,12]
    
    H = htc.HashTableChain(9)
    for i in L:
        H.insert(i)
    H.print_table()
    remove_same_hash(H,1)
    H.print_table()
    remove_same_hash(H,22)
    H.print_table()
    
    print('Question 4')
     
    H = min_heap.MinHeap()
    for i in [4,8,9,14,5,11,7,3,6,10]:
        H.insert(i)
    H.draw()
    for i in range(len(H.heap)+2):
        print(i,sibling(H,i))

    
    print('Question 5')   
    
    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15,12]
    TA = bst.BST()
    for a in A:
        TA.insert(a)
    TA.draw()
    
    B =[ 6, 10, 7, 16, 17, 18, 14, 8, 15]
    TB = bst.BST()
    for a in B:
        TB.insert(a)
    TB.draw()
    
    print(one_child_nodes(TA))
    print(one_child_nodes(TB))
    
   
    print('Question 6')
    
    nums = [6, 3, 23,16, 11, 25, 7,21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
    T = btree.BTree()
    for num in nums:
        T.insert(num)
    T.draw()
    for i in range(4):
        print(data_at_depth_d_or_less(T,i))   
   
    print('Question 7') 
    
    print(missing_pair([2302]))
    print(missing_pair([2,3,0,2,0]))
    L = [7,4,2,8,2,4,7,5,8]
    print(missing_pair(L))
          
   
    print('Question 8')
    
    H = min_heap.MinHeap()
    for i in [4,8,9,14,5,11,7,3,6,10,6]:
        H.insert(i)
    H.draw()
    print(unique_min(H))
    H.insert(3)
    H.draw()
    print(unique_min(H))
 
'''
Program Output:
    
Question 1
1 4 6 7 8 11 12 14 15 16 17 18 
5 7 8 10 14 15 16 17 18 
Question 2
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 18 19 20 21 22 23 24 25 26 28 29 
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 18 19 20 21 22 23 24 25 26 28 30 
Question 3
Table contents:
bucket 0: [ ]
bucket 1: [ [1, ] ]
bucket 2: [ [2, ] [11, ] ]
bucket 3: [ [3, ] [12, ] ]
bucket 4: [ [4, ] [13, ] ]
bucket 5: [ ]
bucket 6: [ [6, ] ]
bucket 7: [ ]
bucket 8: [ ]
Table contents:
bucket 0: [ ]
bucket 1: [ ]
bucket 2: [ [2, ] [11, ] ]
bucket 3: [ [3, ] [12, ] ]
bucket 4: [ [4, ] [13, ] ]
bucket 5: [ ]
bucket 6: [ [6, ] ]
bucket 7: [ ]
bucket 8: [ ]
Table contents:
bucket 0: [ ]
bucket 1: [ ]
bucket 2: [ [2, ] [11, ] ]
bucket 3: [ [3, ] [12, ] ]
bucket 4: [ ]
bucket 5: [ ]
bucket 6: [ [6, ] ]
bucket 7: [ ]
bucket 8: [ ]
Question 4
0 None
1 7
2 4
3 8
4 5
5 9
6 11
7 6
8 14
9 None
10 None
11 None
Question 5
3
4
Question 6
[16]
[6, 11, 16, 21, 25]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29]
Question 7
2302
3
5
Question 8
True
False   
'''