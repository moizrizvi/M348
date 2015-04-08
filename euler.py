import sys
import os
from sympy import *
import numpy as np

def euler_solve(f,a,b,N,p):
    print "Euler\'s method\n"
    h = float((b-a))/float(N)
    t = a
    w = p
    print 'Inital Conditions'
    print 't = {t}\tw = {w}\th={h}\n'.format(t=t,w=w,h=h)
    for i in range(1,N+1):
        print 'w = {w} + {h}*{f}'.format(w=w,h=h,f=f(t,w))
        w = w + h*f(t,w)
        print 't = {a} + {i}*{h}\n'.format(a=a,i=i,h=h)
        t = a + i*h
        print 't = {t}\tw = {w}\n'.format(t=t,w=w)
    return w

def f(t,y):
    return float((1+t))/float((1+y))

a = 1
b = 2
p = 2
N = 2

euler_solve(f,a,b,N,p)

