import matplotlib.pyplot as plt
import numpy as np
import min_heap
import bst
import btree
import hash_table_chain as htc
import math

def has_nodes_with_depth(T,d):
    if type(T) == bst.BST:
        T=T.root
    if T==None:
        return False
    if d==0:
        return True
    return has_nodes_with_depth(T.left,d-1)  or has_nodes_with_depth(T.right,d-1)

def prune_leaves(T):
    if type(T)==btree.BTree:
        T=T.root
    if T.is_leaf:
        T.data = T.data[:2]
    else:
        for c in T.child:
            prune_leaves(c)

def item_status(H,k):
    if H.retrieve(k)==None:
       return -1
    if len(H.bucket[H.h(k)])==1:
        return 0
    return 1

def count_swaps(H,k):
    swaps = 0
    i = len(H.heap)
    while k<H.heap[(i-1)//2].key and i>0:
        swaps+=1
        i = (i-1)//2
    return swaps

def follow_path(T,s):    
    if type(T)==bst.BST:
        T=T.root
    if T==None:
        return None
    if len(s)==0:
        return T.data
    if s[0]=='L':
        return follow_path(T.left,s[1:])
    return follow_path(T.right,s[1:])

def make_bst_n(T):
    t = bst.BSTNode(T.data[0])
    if not T.is_leaf:
       t.left =  make_bst_n(T.child[0])
       t.right =  make_bst_n(T.child[1])
    return t

def make_bst(T):
    Tb = bst.BST()
    Tb.root = make_bst_n(T.root)
    return Tb


def different_words(L):
    H = htc.HashTableChain(len(L))
    count=0
    for w in L:
        if H.insert(w)>0:
            count+=1
    return count 

def try_replace(H,k,m):
    problem = ''
    if k<0 or k > len(H.heap):
        problem = 'k is out of bounds'
    if k>0 and m<H.heap[H.parent(k)].key:
        problem = 'm is smaller than its parent'
    if len(H.heap)>H.leftChild(k) and m>H.heap[H.leftChild(k)].key:
        problem = 'm is larger than its left child'                 
    if len(H.heap)>H.rightChild(k) and m>H.heap[H.rightChild(k)].key:
        problem = 'm is larger than its right child'               
    if problem == '':
        print('heap contents were changed')
        H.heap[k].key = m
    else:
        print('no changes made to the heap because '+problem)

if __name__ == "__main__":
    plt.close('all')
    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
   
    TA = bst.BST()
    for a in A:
        TA.insert(a)
    TA.draw()
    
    print('Question 1')
    for i in range(6):
        print(has_nodes_with_depth(TA,i))
    
    T = btree.BTree()

    nums = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
 
    for num in nums:
        T.insert(num)
    print('Question 2')    
    T.draw()
   
    prune_leaves(T)
    T.draw()
    
    print('Question 3')
    L = [2,4,6,1,2,3,1,12]
    
    H = htc.HashTableChain(len(L))
    for i in L:
        H.insert(i)

    H.print_table()
    print(item_status(H,5))
    print(item_status(H,6))
    print(item_status(H,4))
    print(item_status(H,12))


    print('Question 4')
    H1 = min_heap.MinHeap()
    for i in [1,3,7,8,4,13,9,10]:
        H1.insert(i)
    H1.draw()
    
    print(count_swaps(H1,9))    
    print(count_swaps(H1,5))    
    print(count_swaps(H1,2))    
    print(count_swaps(H1,1))    
    print(count_swaps(H1,0))    
    
    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
   
    TA = bst.BST()
    for a in A:
        TA.insert(a)
    TA.draw()
    
    print('Question 5')
    TA = bst.BST()
    for a in A:
        TA.insert(a)
    
    print(follow_path(TA,''))    
    print(follow_path(TA,'LR'))   
    print(follow_path(TA,'RLR'))  
    print(follow_path(TA,'LRLR'))   
    
    T = btree.BTree()

    nums = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
 
    for num in nums:
        T.insert(num)
    print('Question 6')    
    T.draw()
    Tb = make_bst(T)
    Tb.draw()
    Tb.inOrder()
    
    
    print('Question 7')  
    L =['the','elephants', 'will','rest','for','the','rest','of','the','day']
    print(different_words(L))
    print(different_words(['aa','bb','aa','bb','aa','bb']))
    print(different_words(['data','structures']))
    print(different_words([]))
    
    
    print('Question 8')  
    H1 = min_heap.MinHeap()
    for i in [6, 3, 23,16, 11, 25, 7, 17]:
        H1.insert(i)
    H1.draw() 
    
    try_replace(H1,5,5)
    try_replace(H1,1,12)
    try_replace(H1,3,20)
    try_replace(H1,2,8)
    H1.draw()
    '''
    Question 1
    True
    True
    True
    True
    True
    False
    Question 2
    Question 3
    Table contents:
    bucket 0: [ ]
    bucket 1: [ [1, ] ]
    bucket 2: [ [2, ] ]
    bucket 3: [ [3, ] ]
    bucket 4: [ [4, ] [12, ] ]
    bucket 5: [ ]
    bucket 6: [ [6, ] ]
    bucket 7: [ ]
    -1
    0
    1
    1
    Question 4
    0
    1
    2
    2
    3
    Question 5
    11
    7
    15
    None
    Question 6
    1 6 7 17 18 23 24 
    Question 7
    7
    2
    Question 8
    no changes made to the heap because m is smaller than its parent
    no changes made to the heap because m is larger than its right child
    no changes made to the heap because m is larger than its left child
    heap contents were changed
        
    '''
    
    
    