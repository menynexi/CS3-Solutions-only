import bst
import matplotlib.pyplot as plt

def printSmaller(t,k):
    if t != None:
        printSmaller(t.left,k)
        if k>t.data:
            print(t.data,end=' ')
            printSmaller(t.right,k)

def printLeaves(t):
    if t != None:
        if t.left ==None and t.right== None:
            print(t.data,end=' ')
        else:
            printLeaves(t.left)
            printLeaves(t.right)

def atDepth(t,d):
    if t==None:
        return []
    if d == 0:
        return [t.data]
    return atDepth(t.left,d-1) + atDepth(t.right,d-1)

def depthOfK(t,k):
    if t==None:
        return -1
    if t.data==k:
        return 0
    child = t.left
    if t.data<k:
        child = t.right
    d = depthOfK(child,k)
    if d>=0:
        d+=1
    return d

def tree2List(t):
    if t==None:
        return []
    return tree2List(t.left) + [t.data] + tree2List(t.right)

def list2Tree_n(L):
    if len(L)==0:
        return None
    m = len(L)//2
    return bst.BSTNode(L[m],left=list2Tree_n(L[:m]),right=list2Tree_n(L[m+1:]))
   
def list2Tree(L):
    T = bst.BST()
    T.root = list2Tree_n(L)
    T.size = len(L)
    return T
              
if __name__ == "__main__":

    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
    B =[8, 15, 5, 13, 11, 6, 7, 2, 4, 18, 14]
    
   
    T_empty = bst.BST()
    T_oneNode = bst.BST()
    T_oneNode.insert(23)
    TA = bst.BST()
    for a in A:
        TA.insert(a)
    TB = bst.BST()
    for b in B:
        TB.insert(b)
    

    plt.close('all')
    TA.draw()
    TB.draw()
    
    print('Question 1')
    printSmaller(T_empty.root, 16) 
    print()
    printSmaller(T_oneNode.root, 30) 
    print()
    printSmaller(TA.root, 16) 
    print()
    printSmaller(TA.root, 5)  
    print()
    printSmaller(TB.root, 0)  
    print()
    printSmaller(TB.root, 2302)  
    print()
    
    print('Question 2')
    printLeaves(T_empty.root) 
    print()
    printLeaves(T_oneNode.root) 
    print()
    printLeaves(TA.root) 
    print()
    printLeaves(TB.root) 
    print()
    
    print('Question 3')
    print(atDepth(T_empty.root,2))      
    print(atDepth(T_oneNode.root,0))    
    for i in range(5):
        print(atDepth(TA.root,i))  
        
    for i in range(5):
        print(atDepth(TB.root,i))   
            
    print('Question 4')
    print(depthOfK(T_empty.root,2301))   
    print(depthOfK(T_oneNode.root,0))    
    print(depthOfK(TA.root,11))          
    print(depthOfK(TA.root,6))           
    print(depthOfK(TA.root,18))          
    print(depthOfK(TA.root,21))          
    print(depthOfK(TB.root,11))                       
    
    print('Question 5')
    print(tree2List(TA.root))  
    print(tree2List(TB.root))  
    
    L = [i for i in range(31)]
    
    print('Question 6 - Images')
    Ta = list2Tree(L)
    Ta.draw()

'''
Program Output:
    
Question 1

23 
1 2 4 6 7 8 11 13 14 15 
1 2 4 

2 4 5 6 7 8 11 13 14 15 18 
Question 2

23 
1 4 8 13 15 20 
4 7 11 14 18 
Question 3
[]
[23]
[11]
[6, 16]
[2, 7, 14, 17]
[1, 4, 8, 13, 15, 18]
[20]
[8]
[5, 15]
[2, 6, 13, 18]
[4, 7, 11, 14]
[]
Question 4
-1
-1
0
1
3
-1
3
Question 5
[1, 2, 4, 6, 7, 8, 11, 13, 14, 15, 16, 17, 18, 20]
[2, 4, 5, 6, 7, 8, 11, 13, 14, 15, 18]
Question 6 - Images   
'''        
    