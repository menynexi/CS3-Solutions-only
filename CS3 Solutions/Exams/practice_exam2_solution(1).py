import matplotlib.pyplot as plt
import numpy as np
import min_heap
import bst
import btree
import hash_table_chain as htc
import math

def print_data(T):
    if type(T)==btree.BTree:
        T=T.root
    if T.is_leaf:
        for d in T.data:
            print(d,end=' ')
    else:
        for i in range(len(T.data)):
            print_data(T.child[i])
            print(T.data[i],end=' ')
        print_data(T.child[-1])

def subtract_n(T,n):
    if type(T) == bst.BST:
        T=T.root
    if T!=None:
        subtract_n(T.left,n)
        T.data -= n
        subtract_n(T.right,n)

def prune_leaves(T):
    if type(T)==btree.BTree:
        T=T.root
    if T.child[0].is_leaf:
        T.is_leaf = True
    else:
        for c in T.child:
            prune_leaves(c)


def build_index_table(L):
    H = htc.HashTableChain(len(L))
    for i in range(len(L)):
        p = H.retrieve(L[i])
        if p == None:
            H.insert(L[i],[i])
        else:
            p.append(i)
            H.update(L[i],p)
    return H

def min_key(H):
    if len(H.heap)==0:
        return math.inf
    return H.extractMin().key

def smallest_n(H1,H2,n):
    sl = []
    m1 = min_key(H1)
    m2 = min_key(H2)
    for i in range(n):
        if m1<m2:
           sl.append(m1)
           m1 = min_key(H1)
        else:
           sl.append(m2)
           m2 = min_key(H2)
    return sl

def get_path(T,k):
    if type(T)==bst.BST:
        T=T.root
    if T==None:
        return None
    if T.data == k:
        return ""
    if T.data < k:
        c, turn = T.right, "R"
    else:
        c, turn = T.left, "L"
    p = get_path(c,k)
    if p is not None:
        p = turn+p
    return p

def nodes_with_n_items(T,n):
    if type(T)==btree.BTree:
        T=T.root
    count = 0
    if len(T.data) == n:
        count += 1
    if T.is_leaf:
        return count
    for c in T.child:
        count += nodes_with_n_items(c,n)
    return count

def sum_n(L,k):
    H = htc.HashTableChain(len(L))
    for i in L:
        if H.retrieve(k-i)!=None:
            return True
        H.insert(i)
    return False

def equal_parent_and_child(H):
    for i in range(1,len(H.heap)):
        if H.heap[i].key == H.heap[(i-1)//2].key:
            return True
    return False

if __name__ == "__main__":
    plt.close('all')
    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
    B =[8, 15, 5, 13, 11, 6, 7, 2, 4, 18, 14]
    
   
    TA = bst.BST()
    for a in A:
        TA.insert(a)
    TB = bst.BST()
    for b in B:
        TB.insert(b)
    TA.draw()
    TA.inOrder()
    TB.inOrder()
    subtract_n(TA,3)
    subtract_n(TB,4)
    print('Question 1')
    TA.inOrder()    # -2 -1 1 3 4 5 8 10 11 12 13 14 15 17 
    TB.inOrder()    # -2 0 1 2 3 4 7 9 10 11 14 
    
    
    T = btree.BTree()

    nums = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
 
    for num in nums:
        T.insert(num)
    print('Question 2')    
    T.draw()
    print_data(T)  # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 
    print()
    prune_leaves(T)
    T.draw()
    print_data(T)  # 6 11 17 23 27
    print()
    prune_leaves(T)
    T.draw()
    print_data(T)  # 17
    print()
    
    print('Question 3')
    L = [2,4,6,1,2,3,1,12]
    h = build_index_table(L)
    h.print_table()
    '''
    Table contents:
    bucket 0: [ ]
    bucket 1: [ [1, [3, 6]] ]
    bucket 2: [ [2, [0, 4]] ]
    bucket 3: [ [3, [5]] ]
    bucket 4: [ [4, [1]] [12, [7]] ]
    bucket 5: [ ]
    bucket 6: [ [6, [2]] ]
    bucket 7: [ ]
    '''    
    
    print('Question 4')
    H1 = min_heap.MinHeap()
    for i in [4,8,2,6,3]:
        H1.insert(i)
    H1.draw()
    H2 = min_heap.MinHeap()
    for i in [4,8,9,14,5,7]:
        H2.insert(i)
    H2.draw()
    
    print(smallest_n(H1,H2,5))    # [2,3,4,4,5]
    
    H1 = min_heap.MinHeap()
    for i in [24,8,22,62,3]:
        H1.insert(i)
    H1.draw()
    H2 = min_heap.MinHeap()
    for i in [4,8,9,14,5,7]:
        H2.insert(i)
    H2.draw()
    
    print(smallest_n(H1,H2,4))    # [3, 4, 5, 7]
    
    H1 = min_heap.MinHeap()
    for i in [24,8,22,62,3]:
        H1.insert(i)
    H1.draw()
    H2 = min_heap.MinHeap()
    for i in [4,8,9,14,5,7]:
        H2.insert(i)
    H2.draw()
    
    print(smallest_n(H1,H2,8))    # [3, 4, 5, 7, 8, 8, 9, 14]
    
    H1 = min_heap.MinHeap()
    for i in [24,8,22,62,3]:
        H1.insert(i)
    H1.draw()
    H2 = min_heap.MinHeap()
    for i in [4,8,9,14,5,7]:
        H2.insert(i)
    H2.draw()
    
    print(smallest_n(H1,H2,12))    # [3, 4, 5, 7, 8, 8, 9, 14, 22, 24, 62, inf]
    
    print('Question 5')
    TA = bst.BST()
    for a in A:
        TA.insert(a)
        
    print(get_path(TA, 13)) # RLL
    print(get_path(TA, 8))  # LRR
    print(get_path(TA, 5))  # None
    
    T = btree.BTree()

    nums = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
 
    for num in nums:
        T.insert(num)
    print('Question 6')
    print(nodes_with_n_items(T,1))  #1 
    print(nodes_with_n_items(T,2))  #2    
    print(nodes_with_n_items(T,3))  #2    
    print(nodes_with_n_items(T,4))  #1 
    print(nodes_with_n_items(T,5))  #3 
    
    print('Question 7')
    print(sum_n([2,5,6,3],4))  # False
    print(sum_n([2,5,6,3],7))  # True
    print(sum_n([2,5,6,3],11))  # True
    print(sum_n([2,5,6,3],10))  # False
    
    
    print('Question 8')
    H = min_heap.MinHeap()
    for i in [4,8,9,14,5,7]:
        H.insert(i)
    H.draw()
    
    print(equal_parent_and_child(H))  # False
    H.insert(7)
    print(equal_parent_and_child(H))  # True