import btree
import math
import matplotlib.pyplot as plt

def largestAtDepthD(T,d):
    # Using iteration
    t = T.root
    while d>0:
        if t.is_leaf:
            return -math.inf 
        t=t.child[-1]
        d=d-1
    return t.data[-1]

def largestAtDepthD(t,d):
    # Using recursion
    if type(t)==btree.BTree: 
        t = t.root
    if d==0:
        return t.data[-1]
    if t.is_leaf:
        return -math.inf 
    return largestAtDepthD(t.child[-1],d-1)

def findDepth(t,k):    
    if type(t)==btree.BTree: # t is a BTree object (otherwise it's a BTreeNode)
        t = t.root
    if k in t.data:
        return 0
    if t.is_leaf:
        return -1
    i = 0
    while i<len(t.data) and k>t.data[i]:
        i+=1
    d = findDepth(t.child[i],k)
    if d>=0:
        d+=1
    return d
    
def printAtDepthD(t,d):
    if type(t)==btree.BTree: # t is a BTree object (otherwise it's a BTreeNode)
        t = t.root
    if d==0:
        for item in t.data:
            print(item,end=' ')
    else:
        if not t.is_leaf:
            for c in t.child:
                printAtDepthD(c,d-1)
    
def numLeaves(t):
    if type(t)==btree.BTree: # t is a BTree object (otherwise it's a BTreeNode)
        t = t.root
    if t.is_leaf:
        return 1
    count = 0
    for c in t.child:
        count +=numLeaves(c)
    return count

def fullNodesAtDepthD(t,d):
    if type(t)==btree.BTree: # t is a BTree object (otherwise it's a BTreeNode)
        t = t.root
    if d==0:
        return int(t.is_full())
    if t.is_leaf:
        return 0
    count = 0
    for c in t.child:
        count += fullNodesAtDepthD(c,d-1)    
    return count

def printDescending(t):
    if type(t)==btree.BTree: # t is a BTree object (otherwise it's a BTreeNode)
        t = t.root
    if t.is_leaf:
        for d in t.data[::-1]:
            print(d,end=' ')
    else:
        printDescending(t.child[-1])
        for i in range(len(t.data)-1,-1,-1):
            print(t.data[i],end=' ')
            printDescending(t.child[i])

def printItemsInNode(t,k):
    if type(t)==btree.BTree: # t is a BTree object (otherwise it's a BTreeNode)
        t = t.root
    if k in t.data:
        for d in t.data:
            print(d,end=' ')
        print()
    else:
        if not t.is_leaf:
            i = 0
            while i<len(t.data) and k>t.data[i]:
                i+=1
            printItemsInNode(t.child[i],k)    
            
if __name__ == "__main__":
    plt.close('all')
    
    T = btree.BTree()

    nums = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
  
    t = T.find(4)
    for num in nums:
        T.insert(num)
        
    T2 = btree.BTree()   
    for num in [32,12,58,7,43]:
        T2.insert(num)
        
    
    
    T.draw()
    T2.draw()
    
    print(largestAtDepthD(T,0)) # 17
    print(largestAtDepthD(T,1)) # 27
    print(largestAtDepthD(T,2)) # 30
    print(largestAtDepthD(T,3)) # -inf
    
    print(largestAtDepthD(T2,0)) # 58
    print(largestAtDepthD(T2,1)) # -in
    
    print(findDepth(T,17)) # 0
    print(findDepth(T,11)) # 1
    print(findDepth(T,18)) # 2
    print(findDepth(T,31)) # -1
    
    print(findDepth(T2,7)) # 0
    print(findDepth(T2,61)) # -1
    

    printAtDepthD(T,0) # 17
    print()
    printAtDepthD(T,1) # 6 11 23 27
    print()
    
    print(numLeaves(T))         # 6
    print(numLeaves(T2))        # 1
    
    print(fullNodesAtDepthD(T,0)) # 0
    print(fullNodesAtDepthD(T,1)) # 0
    print(fullNodesAtDepthD(T,2)) # 3
    print(fullNodesAtDepthD(T,3)) # 0
    
    print(fullNodesAtDepthD(T2,0)) # 1
    print(fullNodesAtDepthD(T2,1)) # 0
    
    
    printDescending(T)  # 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 
    print()
    printDescending(T2) # 58 43 32 12 7 
    print()
    
    printItemsInNode(T,3)   # 1 2 3 4 5
    printItemsInNode(T,32)  #
    printItemsInNode(T2,43) # 7 12 32 43 58
    printItemsInNode(T2,20) #