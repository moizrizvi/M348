'''
Write a function that evaluates a polynomial of the form

    P(x) = a_0 + a_1(x-x_0) + ... + a_n(x-x_0)*...*(x-x_(n-1))

Inputs: n,x, vectors <a_i> & <x_i>
Ouputs: P(x)
'''

def eval_polyn(n,x,A,X):
    ret = 0
    ret += A[0]

    P = [0]*n

    P[0] = x - X[0]

    for i in range(1,n):
        P[i] = P[i-1]*(x-X[i])

    for i in range(n):
        ret += A[i+1]*P[i]

    return ret


n = 1
x = 1.5
X = [0,1]
A = [1,1]

print eval_polyn(n,x,A,X)


