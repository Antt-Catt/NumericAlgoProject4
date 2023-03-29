import numpy as np

def Newton_Raphson(f,J,U0,N,epsilon):
    Xn=U0
    if (type(U0)==float)or (type(U0)==int):
        for i in range(N):
            Xn=Xn-f(Xn)/J(Xn)
            if abs(Xn)<epsilon:
                return Xn
        return Xn

    for i in range(N):
        h=np.linalg.lstsq(J(Xn),f(Xn))
        Xn=np.subtract(Xn,h[0])
        if np.linalg.norm(Xn)<epsilon:
            return Xn
    return Xn



'''QUESTION 4'''


def Newton_Raphson_backtrack(f,J,U0,N,epsilon,eps2):
    Xn=U0
    alpha=1
    for i in range(N):
        h=np.linalg.lstsq(J,f(Xn))
        while np.linalg.norm(f(Xn-alpha*h))-np.linalg.norm(f(Xn))>0:
            alpha=alpha*0.5
            if alpha<eps2:
                return False
        Xn=np.substract(Xn,h)
        if np.linalg.norm(Xn)<epsilon:
            return Xn
    return Xn

def poly(x):
    return x**3-x**2

def deri_poly(x):
    return 3*x**2-2*x

