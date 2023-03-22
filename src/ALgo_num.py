import numpy as np
def Newton_Raphson(f,J,U0,N,epsilon):
    Xn=U0
    for i in range(N):
        h=np.linalg.solve(J,f(Xn))
        Xn=np.substract(Xn,h)
        if np.linalg.norm(Xn)<epsilon:
            return Xn
    return Xn