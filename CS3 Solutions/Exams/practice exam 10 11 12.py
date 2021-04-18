import singly_linked_list as sll
import matplotlib.pyplot as plt
import math

def smaller_than_n(t,x):
    if t==None:
        return None
    rest_of_list = smaller_than_n(t.next,x)
    if t.data < x:
        return  sll.ListNode(t.data,rest_of_list)
    return rest_of_list
        
def smaller_than(L,x):
    smaller_list = sll.List()
    smaller_list.head =  smaller_than_n(L.head,x)
    if smaller_list.head == None:
        smaller_list.tail =None
    else:
        t =  smaller_list.head
        while t.next!=None:
            t=t.next
        smaller_list.tail = t
    return smaller_list

def sum_last_n(L,n):
    t, length,sum_l = L.head, 0, 0
    while t!=None:
        sum_l += t.data
        length+=1
        t = t.next
    t = L.head
    for i in range(max([0,length-n])):    
        sum_l -= t.data
        t=t.next
    return sum_l

def middle(L):
    t,mid,advance  = L.head, L.head, False
    while t!=None:
        t = t.next
        if advance:
            mid = mid.next
        advance = ~ advance
    return mid.data

if __name__ == "__main__":
    plt.close('all')

    L3 = sll.List()
    L3.extend([3,6,1,4,0,9,7,4,8,5,9,7,9])
    L3.print()
    L3.draw()
    
    print('Question 10')  
    S1 = smaller_than(L3,6)
    S1.print()
    S1.draw()
   
    print('Question 11')  
    print(sum_last_n(L3,6))
    print(sum_last_n(L3,66))

    print('Question 12')  
    L3 = sll.List()
    for i in range(10):
        L3.append(i)
        L3.print()
        print('middle',middle(L3))
    