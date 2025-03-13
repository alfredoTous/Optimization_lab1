#!/udr/bin/env python3

import numpy as np
import sympy as sp

def taylor_expansion(function,n,a):
    x = sp.symbols("x")
    taylor_expansion = function.subs(x,a)
    derivative = sp.diff(function,x)
    i = 0
    number_of_terms = 0
    while number_of_terms != n:
        i += 1
        if derivative.subs(x,a) == 0:
            pass
        taylor_expansion += (derivative.subs(x,a) /sp.factorial(i)) * (x-a)**i
        derivative = sp.diff(derivative,x)
        number_of_terms += 1
        
        

    return taylor_expansion

x = sp.symbols("x")
print(taylor_expansion(sp.sin(x),5,0))


