import singly_linked_list as sll
import matplotlib.pyplot as plt
import math

def sum_list(L):
    return sum_list_n(L.head)

def sum_list_n(t):
    if t ==None:
        return 0
    return t.data + sum_list_n(t.next)

def max_list(t):
    if type(t) == sll.List:
        t = t.head
    if t==None:
        return -math.inf
    max_l= max_list(t.next)
    if t.data>max_l:
        return t.data
    return max_l

def identical(L1,L2):
    return identical_n(L1.head, L2.head)

def identical_n(t1,t2):
    if t1==None and t2==None: # Both lists are empty, they are equal 
        return True
    if t1==None or t2==None: # Only one list is empty, they are not equal
        return False
    # Neither list is empty
    if t1.data != t2.data:   
        return False
    return identical_n(t1.next,t2.next)

def to_list(t):
    if type(t) == sll.List:
        t = t.head
    if t==None:
        return []
    return [t.data] + to_list(t.next)

def count(L,x): 
    return count_n(L.head,x)

def count_n(t,x): 
    if t==None:
        return 0
    if t.data ==x:
        return 1 + count_n(t.next,x)
    return count_n(t.next,x)

def sum_first_n(t,n):
    if type(t) == sll.List:
        t = t.head
    if t==None or n==0:
        return 0
    return t.data + sum_first_n(t.next,n-1)

def add_n(L,n):
    add_n_n(L.head,n)
    
def add_n_n(t,n):
    if t!=None:
        t.data+=n
        add_n_n(t.next,n)

def is_sorted(t):
    if type(t) == sll.List:
        t = t.head
    if t==None or t.next==None:
        return True
    if t.data>t.next.data:
        return False
    return is_sorted(t.next)
 
def remove_n(t,x):
    # Returns a reference to the list whose first node is t after removing x, if it's in the list
    if t==None:
        return None
    if t.data == x:
        return t.next
    t.next = remove_n(t.next,x)
    return t

def remove(L,x):
    L.head = remove_n(L.head,x)
    # This is almost enough, but if x was the last item in L, L.tail will point to the wrong node 
    # Now we need to make sure tail points to the last element in the list
    if L.head == None:
        L.tail = None
    else:
        if L.tail.data==x:
            t =  L.head
            while t.next!=None:
                t=t.next
            L.tail = t
    
if __name__ == "__main__":
    plt.close('all')
    L1 = sll.List()
    L1.print()
    L1.draw()
    
    L2 = sll.List()
    L2.append(2)
    L2.print()
    L2.draw()
    
    L3 = sll.List()
    L3.extend([3,6,1,4,0,9,7,4,8,5,9,7,9])
    L3.print()
    L3.draw()
    
    print('Question 1')  
    print(sum_list(L1))
    print(sum_list(L2))
    print(sum_list(L3))
    
    print('Question 2')
    print(max_list(L1))
    print(max_list(L2))
    print(max_list(L3))
    
    L4 = sll.List()
    L4.extend([3,6,1,0])
    
    L5 = sll.List()
    L5.extend([3,6,1,4,0,9,7,4,8,5,9,7,9])
    
    print('Question 3')   
    print(identical(L1,L2))
    print(identical(L4,L4))
    print(identical(L5,L3))
    print(identical(L3,L4))
    print(identical(L4,L5))

    print('Question 4')
    print(to_list(L1))
    print(to_list(L2))
    print(to_list(L3))
    print(to_list(L4))
   
    print('Question 5')
    print(count(L1,2)) 
    print(count(L2,2)) 
    print(count(L3,2)) 
    print(count(L3,4)) 
    print(count(L3,9)) 
    
    print('Question 6')
    print(sum_first_n(L1,2))
    print(sum_first_n(L2,2))
    print(sum_first_n(L3,0))      
    print(sum_first_n(L3,6))   
    print(sum_first_n(L3,10)) 
    
    print('Question 7')   
    add_n(L1,3)
    L1.print()
    add_n(L2,4)
    L2.print()
    add_n(L3,5)
    L3.print()
    add_n(L3,1)
    L3.print()
    
    L1 = sll.List()
    L2 = sll.List()
    L2.append(2)
    L3 = sll.List()
    L3.extend([3,6,1,4,0,9,7,4,8,5,9,7,9])
    L4 = sll.List()
    L4.extend([2,3,6,7,8,9])
    L5 = sll.List()
    L5.extend([2,3,6,7,8,9,0])
    
    print('Question 8')   
    print(is_sorted(L1))
    print(is_sorted(L2))
    print(is_sorted(L3))
    print(is_sorted(L4))
    print(is_sorted(L5))
    
    print('Question 9')  
    L1 = sll.List()
    L2 = sll.List()
    L2.append(2)
    L3 = sll.List()
    L3.extend([3,6,1,4,0,9,7,4,8,5,9,7,9])
    L4 = sll.List()
    L4.extend([2,3,6,7,8,9])
    L5 = sll.List()
    L5.extend([2,3,6,7,8,9,0])
    
    for L in [L1,L2,L3,L4,L5]:
        L.print()
    
    remove(L1,5)
    L1.print()
    remove(L2,2)
    L2.print()
    remove(L3,0)
    L3.print()
    remove(L4,2)
    L4.print()
    remove(L5,9)
    L5.print()

'''
[]
[2]
[3, 6, 1, 4, 0, 9, 7, 4, 8, 5, 9, 7, 9]
Question 1
0
2
72
Question 2
-inf
2
9
Question 3
False
True
True
False
False
Question 4
[]
[2]
[3, 6, 1, 4, 0, 9, 7, 4, 8, 5, 9, 7, 9]
[3, 6, 1, 0]
Question 5
0
1
0
2
3
Question 6
0
2
0
23
47
Question 7
[]
[6]
[8, 11, 6, 9, 5, 14, 12, 9, 13, 10, 14, 12, 14]
[9, 12, 7, 10, 6, 15, 13, 10, 14, 11, 15, 13, 15]
Question 8
True
True
False
True
False
Question 9
[]
[2]
[3, 6, 1, 4, 0, 9, 7, 4, 8, 5, 9, 7, 9]
[2, 3, 6, 7, 8, 9]
[2, 3, 6, 7, 8, 9, 0]
[]
[]
[3, 6, 1, 4, 9, 7, 4, 8, 5, 9, 7, 9]
[3, 6, 7, 8, 9]
[2, 3, 6, 7, 8, 0]
'''