import math 
import time
from numpy import *

def equal_functions_int(f1,f2):
    for i in range(1000):
        x = random.randint(-500,501)
        if eval(f1) != eval(f2):
            return False
    return True

def equal_functions_float(f1,f2,tol=0.00001):
    for i in range(1000):
        t = (random.rand()-0.5)*2*math.pi   
        if abs(eval(f1) - eval(f2))>tol:
            return False
    return True

if __name__ == "__main__":  
    random.seed(0)  # Use same seed to obtain repeatable results
    
    f1 = 'x*x + x - 12'
    f2 = '(x+4)*(x-3)'
    f3 = '(x+4)*(x+3)'
    f4 = 'x%11 +1'
    f5 = '(x+1)%11'
    
    f6 = 'tan(t)+1'
    f7 = 'max(.95,sin(t))'
    f8 = 'max(.95,cos(t))'
    f9 = 'sin(t)**2 + cos(t)**2 - 1'
    f10 = 'sin(t)*(1/cos(t) + 1/sin(t))'
    
    
       
    for f in [f1,f2,f3,f4,f5]:
        for g in [f1,f2,f3,f4,f5]:
            print(f+' == '+g,':',equal_functions_int(f,g))
        print()
        
    for f in [f6,f7,f8,f9,f10]:
        for g in [f6,f7,f8,f9,f10]:
            print(f+' == '+g,':',equal_functions_float(f,g))
        print()
        
'''
Program output:
     
x*x + x - 12 == x*x + x - 12 : True
x*x + x - 12 == (x+4)*(x-3) : True
x*x + x - 12 == (x+4)*(x+3) : False
x*x + x - 12 == x%11 +1 : False
x*x + x - 12 == (x+1)%11 : False

(x+4)*(x-3) == x*x + x - 12 : True
(x+4)*(x-3) == (x+4)*(x-3) : True
(x+4)*(x-3) == (x+4)*(x+3) : False
(x+4)*(x-3) == x%11 +1 : False
(x+4)*(x-3) == (x+1)%11 : False

(x+4)*(x+3) == x*x + x - 12 : False
(x+4)*(x+3) == (x+4)*(x-3) : False
(x+4)*(x+3) == (x+4)*(x+3) : True
(x+4)*(x+3) == x%11 +1 : False
(x+4)*(x+3) == (x+1)%11 : False

x%11 +1 == x*x + x - 12 : False
x%11 +1 == (x+4)*(x-3) : False
x%11 +1 == (x+4)*(x+3) : False
x%11 +1 == x%11 +1 : True
x%11 +1 == (x+1)%11 : False

(x+1)%11 == x*x + x - 12 : False
(x+1)%11 == (x+4)*(x-3) : False
(x+1)%11 == (x+4)*(x+3) : False
(x+1)%11 == x%11 +1 : False
(x+1)%11 == (x+1)%11 : True

tan(t)+1 == tan(t)+1 : True
tan(t)+1 == max(.95,sin(t)) : False
tan(t)+1 == max(.95,cos(t)) : False
tan(t)+1 == sin(t)**2 + cos(t)**2 - 1 : False
tan(t)+1 == sin(t)*(1/cos(t) + 1/sin(t)) : True

max(.95,sin(t)) == tan(t)+1 : False
max(.95,sin(t)) == max(.95,sin(t)) : True
max(.95,sin(t)) == max(.95,cos(t)) : False
max(.95,sin(t)) == sin(t)**2 + cos(t)**2 - 1 : False
max(.95,sin(t)) == sin(t)*(1/cos(t) + 1/sin(t)) : False

max(.95,cos(t)) == tan(t)+1 : False
max(.95,cos(t)) == max(.95,sin(t)) : False
max(.95,cos(t)) == max(.95,cos(t)) : True
max(.95,cos(t)) == sin(t)**2 + cos(t)**2 - 1 : False
max(.95,cos(t)) == sin(t)*(1/cos(t) + 1/sin(t)) : False

sin(t)**2 + cos(t)**2 - 1 == tan(t)+1 : False
sin(t)**2 + cos(t)**2 - 1 == max(.95,sin(t)) : False
sin(t)**2 + cos(t)**2 - 1 == max(.95,cos(t)) : False
sin(t)**2 + cos(t)**2 - 1 == sin(t)**2 + cos(t)**2 - 1 : True
sin(t)**2 + cos(t)**2 - 1 == sin(t)*(1/cos(t) + 1/sin(t)) : False

sin(t)*(1/cos(t) + 1/sin(t)) == tan(t)+1 : True
sin(t)*(1/cos(t) + 1/sin(t)) == max(.95,sin(t)) : False
sin(t)*(1/cos(t) + 1/sin(t)) == max(.95,cos(t)) : False
sin(t)*(1/cos(t) + 1/sin(t)) == sin(t)**2 + cos(t)**2 - 1 : False
sin(t)*(1/cos(t) + 1/sin(t)) == sin(t)*(1/cos(t) + 1/sin(t)) : True      

'''  