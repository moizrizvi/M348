#python2.7
import sys
import os
from sympy import *
import numpy as np
from math import log, e, cos, sin, pi

def trapezoid(f, x_0, x_1):
    print 'Trapezoid Rule\n'
    h = x_1 - x_0
    f_0 = f(x_0)
    f_1 = f(x_1)
    ans = (float(h)/float(2)) * (f_0 + f_1)
    print 'h = {x_1} - {x_0} = {h}\n'.format(x_1 = x_1, 
                                           x_0 = x_0, 
                                           h   = h)

    print '''h/2[f(x_0) + f(x_1)] = {h}/2[f({x_0}) + f({x_1})] 
                     = {h_2} ({f_0} + {f_1})
                     = {ans}'''.format(x_0=x_0,
                                       x_1=x_1,
                                       h=h,
                                       h_2=h/2,
                                       f_0=f_0,
                                       f_1=f_1,
                                       ans=ans)
    return ans

def simpson(f, x_0, x_2):
    print 'Simpson\'s Rule\n'
    h = float(x_2 - x_0)/float(2)
    x_1 = x_0 + h
    f_0 = f(x_0)
    f_1 = f(x_1)
    f_2 = f(x_2)
    ans = (float(h)/float(3)) * (f_0 + 4*f_1 + f_2)
    print 'h = ({x_1} - {x_0})/2 = {h}\n'.format(x_1 = x_1, 
                                                 x_0 = x_0, 
                                                 h   = h)
    print '''h/3[f(x_0) + 4*f(x_1) + f(x_2)] = {h}/3[f({x_0}) + 4*f({x_1}) + f({x_2})] 
                                = {h_3} ({f_0} + 4*{f_1} + {f_2})
                                = {ans}'''.format(x_0=x_0,
                                                    x_1=x_1,
                                                    x_2=x_2,
                                                    h  =h,
                                                    h_3=h/3,
                                                    f_0=f_0,
                                                    f_1=f_1,
                                                    f_2=f_2,
                                                    ans=ans)
    return ans


def f(x):
    return float(1)/(float(x)*float(log(x)))

# print trapezoid(f, e, e+1)
# print simpson(f, e, e+1)

def comp_trapezoid_print(f, a, b, n):
    print 'Composite Trapezoid Rule\n'
    h = float(b - a)/float(n)
    s = 0
    for i in range(1,n):
        s += f(a + i*h)
    ans = float(h)/float(2)*(f(a) + 2*s + f(b))
    print '''h/2[f(a) + 2*SUM(f(x_j)) + f(b)] = {h}/2[f({a}) + 2*{s} + f({b})] 
                                 = {h_2} ({f_a} + {s_2} + {f_b})
                                 = {ans}\n'''.format(a=a,
                                                  b=b,
                                                  s=s,
                                                  h  =h,
                                                  h_2=h/2,
                                                  f_a=f(a),
                                                  f_b=f(b),
                                                  s_2=s*2,
                                                  ans=ans)
    return ans

def comp_trapezoid(f, a, b, n):
    h = float(b - a)/float(n)
    s = 0
    for i in range(1,n):
        s += f(a + i*h)
    ans = float(h)/float(2)*(f(a) + 2*s + f(b))
    return ans

f = lambda x: sin(x)
a = 0
b = pi/2

a_1 = comp_trapezoid(f, a, b, 4)
a_2 = comp_trapezoid(f, a, b, 8)
# print a_1
# print a_2
# print a_2 - a_1


def comp_simpson(f, a, b, n):
    print 'Composite Simpson Rule\n'
    h = float(b - a)/float(n)
    x_0 = f(a) + f(b)
    print 'x_0 = %d' % x_0
    x_1 = 0
    x_2 = 0
    x = 0
    for i in range(1,n):
        print 'i = %d' % i
        x = a + i*h
        print 'x = %f' % x
        print 'f(x) = %f' % f(x) 
        if(i % 2 == 0):
            x_2 += f(x)
            print 'x_2 + f(x) = %f' % x_2
        else:
            x_1 += f(x)
            print 'x_1 + f(x) = %f' % x_1
    ans = float(h*(x_0 + 2*x_2 + 4*x_1))/float(3)
    print
    print '   h(x_0 + 2*x_2 + 4*x_1)/3'
    print ''' = {h}({x_0} + 2*{x_2} + 4*{x_1})/3'''.format(h=h,
                                                        x_0=x_0, 
                                                        x_2=x_2, 
                                                        x_1=x_1)
    print ' = {ans}'.format(ans=ans)



def g(x):
    return cos(x)**2

# comp_trap(g, -0.5, 0.5, 4)
# comp_simpson (g, -0.5, 0.5, 4)


def romberg(f, a, b):
    print 'Romberg Integration\n'
    h = b - a
    print 'h = %f\n' % h

    R_1_1 = float(h)/float(2)*(f(a) + f(b))
    print 'R_1_1 = h/2(f(a) + f(b))'
    print 'R_1_1 = %f\n' % R_1_1

    R_2_1 = comp_trapezoid(f, a, b, 1)
    print 'R_2_1 = comp_trapezoid(f, a, b, 1)'
    print 'R_2_1 = %f\n' % R_2_1

    R_3_1 = comp_trapezoid(f, a, b, 2)
    print 'R_3_1 = comp_trapezoid(f, a, b, 2)'
    print 'R_3_1 = %f\n' % R_3_1

    R_2_2 = R_2_1 + (float(1)/float(3))*(R_2_1 - R_1_1)
    print 'R_2_2 = R_2_1 + (1/3)(R_2_1 - R_1_1)'
    print 'R_2_2 = {R_2_1} + (1/3)({R_2_1} - {R_1_1})'.format(R_2_1=R_2_1,
                                                              R_1_1=R_1_1)
    print 'R_2_2 = %f\n' % R_2_2

    R_3_2 = R_3_1 + (float(1)/float(3))*(R_3_1 - R_2_1)
    print 'R_3_2 = R_3_1 + (1/3)(R_3_1 - R_2_1)'
    print 'R_3_2 = {R_3_1} + (1/3)({R_3_1} - {R_2_1})'.format(R_3_1=R_3_1,
                                                              R_2_1=R_2_1)
    print 'R_3_2 = %f\n' % R_3_2

    R_3_3 = R_3_2 + (float(1)/float(15))*(R_3_2 - R_2_2)
    print 'R_3_3 = R_3_2 + (1/15)*(R_3_2 - R_2_2)'
    print 'R_3_3 = {R_3_2} + (1/15)*({R_3_2} - {R_2_2})'.format(R_3_2=R_3_2,
                                                                R_2_2=R_2_2)
    print 'R_3_3 = %f' % R_3_3




def h(x):
    return x**2 * e**(-x)

# romberg(h, 0, 1)

def number7():
    fx_1 = 2.4142
    fx_2 = 2.6734
    fx_3 = 2.8974
    fx_4 = 3.0976
    fx_5 = 3.2804

    h = 5 - 1
    R_1_1 = float(h)/float(2)*(2.4142 + 3.2804)
    print 'R_1_1 = h/2(f(a) + f(b))'
    print 'R_1_1 = {h}/2({fx_1} + {fx_5})'.format(h=h,
                                                  fx_1=fx_1,
                                                  fx_5=fx_5)
    print 'R_1_1 = %f\n' % R_1_1

    R_2_1 = float(h/2)/float(2)*(2.4142 + 2*2.8974 + 3.2804)
    print 'R_2_1 = (h/2)/2*(2.4142 + 2*2.8974 + 3.2804)'
    print 'R_2_1 = %f\n' % R_2_1

    R_3_1 = float(h/4)/float(2)*(2.4142 + 2*(2.8974+2.6734+3.0976) + 3.2804)
    print 'R_3_1 = (h/4)/2*(2.4142 + 2*(2.8974+2.6734+3.0976) + 3.2804)'
    print 'R_3_1 = %f\n' % R_3_1

    R_2_2 = R_2_1 + (float(1)/float(3))*(R_2_1 - R_1_1)
    print 'R_2_2 = R_2_1 + (1/3)(R_2_1 - R_1_1)'
    print 'R_2_2 = {R_2_1} + (1/3)({R_2_1} - {R_1_1})'.format(R_2_1=R_2_1,
                                                              R_1_1=R_1_1)
    print 'R_2_2 = %f\n' % R_2_2

    R_3_2 = R_3_1 + (float(1)/float(3))*(R_3_1 - R_2_1)
    print 'R_3_2 = R_3_1 + (1/3)(R_3_1 - R_2_1)'
    print 'R_3_2 = {R_3_1} + (1/3)({R_3_1} - {R_2_1})'.format(R_3_1=R_3_1,
                                                              R_2_1=R_2_1)
    print 'R_3_2 = %f\n' % R_3_2

    R_3_3 = R_3_2 + (float(1)/float(15))*(R_3_2 - R_2_2)
    print 'R_3_3 = R_3_2 + (1/15)*(R_3_2 - R_2_2)'
    print 'R_3_3 = {R_3_2} + (1/15)*({R_3_2} - {R_2_2})'.format(R_3_2=R_3_2,
                                                                R_2_2=R_2_2)
    print 'R_3_3 = %f' % R_3_3

number7()



