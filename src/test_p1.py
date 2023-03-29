from part_1 import *
import time
import numpy as np
#QUESTION 3

print("TEST...")
print("")

print("Testing scalar...")
print("")
time.sleep(0.25)
def function(x):
    return x*x-4

def deri(x):
    return 2*x

def function2(x):
    return x**3-x**2


def deri2(x):
    return 3*x**2-2*x

start,eps,N=1.1,0.01,100
eps2=0.75
print("Solution de la fonction f:x-> x**2 - 4 avec U0="+str(start)+" epsilon = "+str(eps)+" : "+str(Newton_Raphson(function,deri,start,N,eps)))
print("Solution de la fonction f:x-> x**3-x**2 avec U0="+str(start)+" epsilon = "+str(eps)+" : "+str(Newton_Raphson(function2,deri2,start,N,eps)))



time.sleep(0.25)
print("")


print("Testing matrixes...")
print("")

def f_mat_1(X):
    return ((X[0]+X[1])/2,(X[0]-X[1])/2)

def J_1(Xn):
    Jacobian=np.zeros((2,2))
    Jacobian[0][1]=0.5
    Jacobian[0][0]=0.5
    Jacobian[1][0]=0.5
    Jacobian[1][1]=-0.5
    return Jacobian

time.sleep(0.25)

print("Solving f(u,v)-> ((u+v)/2,(u-v)/2)=(0,0)")
print("starting point : [1,1]")
start_mat=np.ones(2)
print("Vector solution : ")
print(Newton_Raphson(f_mat_1,J_1,start_mat,N,eps))
print("")
time.sleep(0.25)

def f_mat_2(X):
    return (((X[0]+X[1])**2)/2-5,((X[0]-X[1])**2)/2)

def J_2(Xn):
    Jacobian=np.zeros((2,2))
    Jacobian[0][0]=Xn[0]*(Xn[0]+Xn[1])
    Jacobian[0][1]=Xn[1]*(Xn[0]+Xn[1])
    Jacobian[1][1]=Xn[0]*(Xn[0]-Xn[1])
    Jacobian[1][0]=-Xn[1]*(Xn[0]-Xn[1])
    return Jacobian

print("Solving f(u,v)-> ((u+v)**2/2-5,(u-v)**2/2)=(0,0)")
print("starting point : [1,1]")
start_mat=np.ones(2)
print("Vector solution : ")
print(Newton_Raphson(f_mat_2,J_2,start_mat,100,eps))



#print("Solution :"+str(Newton_Raphson()))



#QUESTION 4
print("")
print("QUESTION 4...")
time.sleep(0.5)
print("")


alph=1
def function3(x):
    return x**alph
def deri3(x):
    return alph*(x**(alph-1))

liste=[]

for i in range(1,250):
    if abs(Newton_Raphson(function3,deri3,start,N,eps))>(10*eps):
        liste.append(alph)
        break
    alph+=1
print("With the following parameters N="+str(N)+" epsilon="+str(eps)+" starting point x0="+str(start) )
print("minimum exponent that makes error = 10*epsilon is : ",min(liste))
print("The function that isn't found with Newton Raphson : f(x)-> 1-x**"+str(alph))
print("The solution proposed by Newton Raphson is : ")
print(Newton_Raphson(function3,deri3,start,N,eps))
print(" In theory, the solution is 0...")

print("")
print("Compared to Newton_raphson_bactrack : ")
print(Newton_Raphson_backtrack(function3,deri3,start,N,eps,eps2))


#print("Solution de la fonction f:x-> x**2 avec U0=",start,"epsilon = ",epsilon," : ","epsilon2 ( bactracking) = ",Newton_Raphson_backtrack(function,deri,start,N,eps,eps2))
#print("Solution de la fonction f:x-> x**3-x**2 avec U0=",start,"epsilon = ",epsilon,"epsilon2 ( bactracking) = ",eps2," : ",Newton_Raphson_backtrack(function2,deri2,start,eps,eps2))

