#python 2.7
import sys
import os
from sympy import *
import numpy as np
from math import sin, e, cos

'''
Returns N_3(h) for function f at x_0
'''

def N_3(f,h,x_0):

    def N_1(f,h,x_0):
        return (1/(2*h))*(f(x_0+h) -f (x_0-h))

    A = [h,h/2,h/4]

    N = list()

    for i in range(3):
        n = N_1(f, A[i], x_0)
        print 'N_1({h}) = {val}'.format(h=A[i],val=n)
        N.append(n)

    a =  float(N[1] + float(1)/float(3)*float(N[1] - N[0]))
    b = float(N[2] + float(1)/float(3)*float(N[2] - N[1]))

    print 'N_2({h}) = {val}'.format(h=h, val=a)
    print 'N_2({h}) = {val}'.format(h=h/2, val=b)

    N_3 = b + float(1)/float(15) * (b-a)

    print 'N_3({h}) = {val}'.format(h=h, val=N_3)


if __name__ == '__main__':
    y_inp, h_inp, x_0_inp = None, None, None
    while not all([y_inp, h_inp, x_0_inp]):
        try:
            y_inp = raw_input('Input equation: ')
            h_inp = input('Input step size: ')
            x_0_inp = input('Input x value: ')
        except SyntaxError:
            print 'try again'
            continue

    x = Symbol('x')
    y = sympify(y_inp)

    f = lambdify(x, y, 'numpy')
    h = float(h_inp)
    x_0 = float(x_0_inp)
    N_3(f,h,x_0)


