import math

def sum_list(L):
    if len(L) == 0:
        return 0
    else:
        return L[0] + sum_list(L[1:])
    
def is_in_list(A,a):
    if len(A) == 0:
        return False
    else:
        if A[0]==a:
            return True
        else:
            return is_in_list(A[1:],a) 
    
def smallest(L):
    if len(L) == 0:
        return math.inf
    else:
        s = smallest(L[1:])
        if L[0]<s:
            return L[0]
        else:
            return s   
        
def binary(n):
    if n<2:
        return str(n)
    else:
        return binary(n//2)+str(n%2)
    
def identical(L1,L2):
    if len(L1)==0 and len(L2)==0: # If both lists are empty, return True
        return True
    if len(L1)==0 or len(L2)==0:  # If one of the lists is empty, return False
        return False
    if L1[0]!=L2[0]:
        return False
    return identical(L1[1:],L2[1:])

if __name__ == "__main__":  
    L = [4,1,7,9,3,0,6,5,2,8]
    print(L)
    
    print('Question 1')
    print(sum_list([]))
    print(sum_list(L))
    print(sum_list(L[2:6]))
    
    print('Question 2')
    print(is_in_list([],2302))
    print(is_in_list(L,3))
    print(is_in_list(L,13))
    print(is_in_list(L,4))
    print(is_in_list(L,8))
    
    print('Question 3')
    print(smallest([]))
    print(smallest(L))
    print(smallest(L[:5]))
    
    print('Question 4')
    print(binary(0))
    print(binary(1))
    print(binary(8))
    print(binary(15))
    print(binary(2302))
    
    print('Question 5')
    print(identical([],[2,4,5,7]))
    print(identical([],[]))
    print(identical([2,4,5],[2,4,5,7]))
    print(identical([2,4,5],[2,4,6]))
    print(identical([2,3,5,5,6],[2,3,5,5]))
    print(identical([2,4,5],[2,4,5]))
   
'''
Program output:
[4, 1, 7, 9, 3, 0, 6, 5, 2, 8]
Question 1
0
45
19
Question 2
False
True
False
True
True
Question 3
inf
0
1
Question 4
0
1
1000
1111
100011111110
Question 5
False
True
False
False
False
True
'''