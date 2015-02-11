#python 2.7

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

def f(x):
    return x**3 + x - 1

def df(x):
    return 3*x**2 + 1

tol = float(10**-4)

p = float(0)

newton_solve(f,df,p,tol)
