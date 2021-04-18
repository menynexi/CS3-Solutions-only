import matplotlib.pyplot as plt
import numpy as np
import min_heap

def is_heap(L):
    for i in range(1,len(L)):
        if L[i]<L[(i-1)//2]:
            return False
    return True

def second(H):
    if len(H.heap)<2:
        return None
    if len(H.heap)==2:
        return H.heap[1].key
    return min(H.heap[1].key,H.heap[2].key)

def height(H):
    # O(log n) solution
    count = 0
    n = len(H.heap)-1
    while n>0:
        n = (n-1)//2
        count+=1
    return count

def height1(H):
    # O(1) solution
    if len(H.heap)==0:
        return 0
    return int(np.log2(len(H.heap)))

def path(H,k):
    p=[H.heap[k].key]
    while k>0:
        k=H.parent(k)
        p.append(H.heap[k].key)
    return p

def equal_siblings(H):
    for i in range(2,len(H.heap),2):
        if H.heap[i].key == H.heap[i-1].key:
            return True
    return False

if __name__=="__main__":
    plt.close('all')
    L0 = [1, 2, 3, 4, 5, 1]
    L1 = [i for i in range(10)]
    L2 = [2302]
    L3 = []
    L4 = [1, 2, 3, 4, 5, 3]
    L5 = [2, 2]
    L6 = [ 2, 2, 1]
    print('-- is_heap')
    for L in [L0,L1,L2,L3,L4,L5,L6]:
        print(is_heap(L))
    
    H1 = min_heap.MinHeap()
    for i in [4,8,2]:
        H1.insert(i)
    H1.draw()
    H2 = min_heap.MinHeap()
    for i in [4,8,9,14,5,7]:
        H2.insert(i)
    H2.draw()
    H3 =  min_heap.MinHeap()
    for i in [4,6,11,8,9,14,5,0,3,7,4]:
        H3.insert(i)
    H3.draw()
    
    H4 =  min_heap.MinHeap()
    for i in [5,0,3,7,8,9,14,4,6,8,9,14,5,6,7,6]:
        H4.insert(i)
    H4.draw()
    
    print('-- second')
    for H in [H1,H2,H3,H4]:
        print(second(H))
        
    print('-- height')
    for H in [H1,H2,H3,H4]:
        print(height(H))
        
    print('-- height')
    for H in [H1,H2,H3,H4]:
        print(height1(H))
        
    print('-- path')
    for i in [0,2,4,12,15]:
        print(path(H4,i))    
        
    print('-- equal_siblings')
    for H in [H1,H2,H3,H4]:
        print(equal_siblings(H))    
     
'''
Program output
-- is_heap
False
True
True
True
True
True
False
-- second
4
5
3
3
-- height
1
2
3
4
-- height
1
2
3
4
-- path
[0]
[3, 0]
[8, 4, 0]
[9, 5, 3, 0]
[7, 6, 5, 4, 0]
-- equal_siblings
False
False
True
True        
'''   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        