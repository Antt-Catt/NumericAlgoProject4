import numpy as np


def  E(X):
    s= 0
    for x in X :
        s1 = 0
        for y in X : 
            if x !=y :
                s1 += np.log(abs(x-y))
        s += np.log(abs(x+1)) +np.log(abs(x-1)) +1/2 * s1
    return s

def derivativeE(X,i):
    s=0
    for xj in X :
        if xj != X[i] :
            s+= 1/(X[i]-xj)            
    return 1/(X[i]+1) + 1/(X[i]-1) + 1/2*s
            


def gradE(X) :
    return [derivativeE(X, i) for i in range(len(X))]

def jacobGradE(X):
    N=len(X)
    J=np.zeros((N,N))
    for i in range(N) :
        for j in range(N) :
            if i == j :
                s=0
                for xj in X :
                    if xj != X[i] :
                        s+= 1/((X[i]-xj)**2)  
                J[i][i]=-1/((X[i]+1)**2) - 1/((X[i]-1)**2) - 1/2*s
            else:
                J[i][j]=1/((X[i]-X[j])**2)
    return J



#test
A= np.linspace(-1, 1,10)
J=jacobGradE(A)