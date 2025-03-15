#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

x = sp.symbols("x")

def taylor_expansion(function,n,a):
    global x
    taylor_expansion = function.subs(x,a)
    derivative = sp.diff(function,x)
    i = 0
    number_of_terms = 0
    while number_of_terms != n:
        i += 1
        if derivative.subs(x,a) != 0:
            taylor_expansion += (derivative.subs(x,a) /sp.factorial(i)) * (x-a)**i
            number_of_terms += 1
        derivative = sp.diff(derivative,x) 
        
    return taylor_expansion



def graph(function, taylor_expansion, x_min_range, x_max_range):
    x_vals = np.linspace(x_min_range, x_max_range, 400)
    
    function_lambdified = sp.lambdify(x, function, 'numpy')
    taylor_lambdified = sp.lambdify(x, taylor_expansion, 'numpy')

    y_vals = function_lambdified(x_vals)
    y_taylor_vals = taylor_lambdified(x_vals)

    plt.plot(x_vals, y_vals, label="Función Original", color="blue")
    plt.plot(x_vals, y_taylor_vals, label="Serie de Taylor", linestyle="--", color="red")
    
    plt.ylim(-2.5, 2.5)  
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()

    img_path = "actual_plot.png"
    plt.savefig(img_path)
    plt.close()  

    return img_path  




