
# Call expressions 

max(7.5, 9.5)

import math

def absolute(x):
    
    if x < 0:
        y = -x # assignment 
    else:
        y = x

    return y

absolute(absolute(-2))

def hello(x):
    return x

two = hello(2)
three = print(3)