#python 2.7
import sys
import os
from sympy import *
import numpy as np

def newton_solve(f, df, p, tol):
    i = 1
    x = p
    MAX = 99999
    while i <= MAX:
        x = p - f(p)/df(p)
        if abs(x - p) < tol:
            print x
            return
        i += 1
        p = x
    print 'Method failed with 99999 iterations.'


if __name__ == '__main__':
    x = Symbol('x')
    y = sympify(sys.argv[1])
    yprime = y.diff(x)
    
    f = lambdify(x, y, 'numpy')
    df = lambdify(x, yprime, 'numpy')
    p = float(0)
    tol = 10**-3
    newton_solve(f,df,p,tol)
