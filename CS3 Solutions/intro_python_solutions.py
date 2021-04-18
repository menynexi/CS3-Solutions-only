# Introduction to Python exercise
# Rename this file to lastname_firstname.py before submitting
import numpy as np

def divisible(a,b):
    return a%b == 0
    
def prime(n):
    if n<=1:
        return False
    for i in range(3,int(np.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def sum_digits(n):
    sum_d = 0
    while n>0:
        sum_d += n%10
        n = n//10
    return  sum_d

def reverse(s):
    rev =''
    for c in s:
        rev = c+ rev
    return  rev

def remove_vowels(s):
    rv =''
    for c in s:
        if not c in 'aeiou':
            rv = rv+ c
    return  rv

def pal(s):
    for i in range(len(s)//2):
        if s[i]!=s[-i-1]:
            return False
    return True

def max_array(A):
    mx = A[0]
    for a in A[1:]:
        if a>mx:
            mx =a
    return mx

def replace_array(A,i,j):
    A[A==i] = j

def is_square(A):
    return len(A.shape)==2 and A.shape[0] == A.shape[1]

def diagonal_sum(A):
    s = 0
    for i in range(A.shape[0]):
        s+= A[i,i]
    return s

def sec_diagonal_sum(A):
    s = 0
    for i in range(A.shape[0]):
        s+= A[i,-1-i]
    return s

def diagonal(A):
    d = np.zeros(A.shape[0],dtype=type(A))
    for i in range(A.shape[0]):
        d[i]= A[i,i]
    return d

def sec_diagonal(A):
    d = np.zeros(A.shape[0],dtype=type(A))
    for i in range(A.shape[0]):
        d[i]= A[i,-1-i]
    return d

def greater_than_list(L,x):
    G = []
    for i in L:
        if i>x:
            G.append(i)
    return G

if __name__ == "__main__":
    
    print('Question 1')
    print(divisible(8,2))       # True
    print(divisible(8,3))       # False
    print(divisible(105,3))     # True
    print(divisible(105,9))     # False
    
    print('Question 2')
    print(prime(2))             # True
    print(prime(49))            # False
    print(prime(151))           # True
    print(prime(39203))         # False
    
    print('Question 3')
    print(sum_digits(2))             # 2
    print(sum_digits(49))            # 13
    print(sum_digits(151))           # 7
    print(sum_digits(39203))         # 17
    
    print('Question 4')
    print(reverse('UTEP'))             # PETU
    print(reverse('racecar'))          # racecar
    print(reverse('W'))                # W 
    print(reverse('Week'))             # keeW 
    
    print('Question 5')
    print(remove_vowels('UTEP'))       # UTEP
    print(remove_vowels('racecar'))    # rccr 
    print(remove_vowels('Week'))       # Wk 
    print(remove_vowels('miners'))     # mnrs 
    
    print('Question 6')
    print(pal('UTEP'))             # False
    print(pal('racecar'))          # True
    print(pal('W'))                # True 
    print(pal('Week'))             # False
    
    
    print('Question 7')
    A0 = np.array([2,5,7,1,2,5,7,8,9,0])
    A1 = np.array([2,5,7,1,2,5,7,0])
    A2 = np.array([2,5,7,11,2,5,7,8,9,0])
    A3 = np.array([2,5,3,0])
    print(max_array(A0))                  # 9
    print(max_array(A1))                  # 7
    print(max_array(A2))                  # 11
    print(max_array(A3))                  # 5
    
    print('Question 10')
    A = np.array([2,5,7,1,2,5,7,8,9,0])
    replace_array(A,5,2302)
    print(A)                    # [   2 2302    7    1    2 2302    7    8    9    0]
    replace_array(A,5,0)
    print(A)                    # [   2 2302    7    1    2 2302    7    8    9    0]
    replace_array(A,7,-1)
    print(A)                    # [   2 2302   -1    1    2 2302   -1    8    9    0]
    replace_array(A,8,-8)
    print(A)                    # [   2 2302   -1    1    2 2302   -1   -8    9    0]
        
    print('Question 11')
    A = np.arange(25).reshape((5,5))
    B = np.array([2,5,7,1,2,7,8,9,0]).reshape((3,3))
    C = np.arange(30).reshape((6,5))
    D = np.array([2,5,7,1,2,7,8,9,0,10]).reshape((2,5))
    print(is_square(A))
    print(is_square(B))
    print(is_square(C))
    print(is_square(D))
    
    print('Question 12')
    A = np.arange(25).reshape((5,5))
    print(A)
    B = np.array([2,5,7,1,2,7,8,9,0]).reshape((3,3))
    print(B)
    print(diagonal_sum(A))        # 60
    print(diagonal_sum(A-12))     # 0
    print(diagonal_sum(B))        # 4
    print(diagonal_sum(B+2))      # 10
    
    print('Question 13')
    A = np.arange(25).reshape((5,5))
    print(A)
    B = np.array([2,5,7,1,2,7,8,9,0]).reshape((3,3))
    print(B)
    print(sec_diagonal_sum(A))        # 60
    print(sec_diagonal_sum(A-12))     # 0
    print(sec_diagonal_sum(B))        # 17
    print(sec_diagonal_sum(B+2))      # 23
    
    print('Question 14')
    A = np.arange(25).reshape((5,5))
    print(A)
    B = np.array([2,5,7,1,2,7,8,9,0]).reshape((3,3))
    print(B)
    print(diagonal(A))        # [0 6 12 18 24]
    print(diagonal(A-12))     # [-12 -6 0 6 12]
    print(diagonal(B))        # [2 2 0]
    print(diagonal(B+2))      # [4 4 2]
    
    print('Question 15')
    A = np.arange(25).reshape((5,5))
    print(A)
    B = np.array([2,5,7,1,2,7,8,9,0]).reshape((3,3))
    print(B)
    print(sec_diagonal(A))        # [4 8 12 16 20]
    print(sec_diagonal(A-12))     # [-8 -4 0 4 8]
    print(sec_diagonal(B))        # [7 2 8]
    print(sec_diagonal(B+2))      # [9 4 10]
    
    
    print('Question 19')
    Ls = [2,5,7,1,2,5,7,8,9,0]
    print(greater_than_list(Ls,4))  # [5, 7, 5, 7, 8, 9]
    print(greater_than_list(Ls,9))  # []
    print(greater_than_list(Ls,-1))  # [2, 5, 7, 1, 2, 5, 7, 8, 9, 0]
    print(greater_than_list(Ls,7))  # [8, 9]