import numpy as np
import matplotlib.pyplot as plt
import math
import singly_linked_list as sll

def equal_neighbors(L):
    if len(L)<2:
        return False
    if L[0]==L[1]:
        return True
    return equal_neighbors(L[1:])
    
def crop(I,k):
    return I[k:-k,k:-k]
                             
def first_and_last_equal(L):
    return L.head == L.tail or L.head.data == L.tail.data

def all_equal(L):
    if L.head == None:
        return True
    t = L.head
    while t!=None:
        if t.data!=L.head.data:
            return False
        t = t.next
    return True

if __name__ == "__main__":  
    plt.close('all')
    L = [4,1,7,9,3,0,6,5,2,8,4,5,6,4]
   
    print('Question 1')
    print(equal_neighbors([]))
    print(equal_neighbors([1]))
    print(equal_neighbors([1,5,6,9,2,9,9]))
    print(equal_neighbors([1,5,6,9,2,9]))
    print(equal_neighbors([1,5,6,9,2,2,9,7]))
    
    print('Question 2')
    img = plt.imread('UTEP.JPG').astype(float)/255
    #fig, ax = plt.subplots(2)
    plt.figure(0)
    plt.imshow(img)
    plt.figure(1)
    plt.imshow(crop(img,100))
    plt.savefig('crop_100')
    plt.figure(2)
    plt.imshow(crop(img,200))
    plt.savefig('crop_200')
    
    L1 = sll.List()
    
    L2 = sll.List()
    L2.append(2)
   
    L3 = sll.List()
    L3.extend([3,6,1,4,0,9,7,4,8,5,9,7,9])
    
    L4 = sll.List()
    L4.extend([3,3,9])
   
    L5 = sll.List()
    L5.extend([3,3,3])
    
    L6 = sll.List()
    L6.extend([9,7,4,8,5,9,7,9])
    
    print('Question 3')
    for L in [L1,L2,L3,L4,L5,L6]:
        print(first_and_last_equal(L))
        
    print('Question 4')
    for L in [L1,L2,L3,L4,L5,L6]:
        print(all_equal(L))
            