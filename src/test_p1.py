from part_1 import *
import time
import numpy as np
#QUESTION 3

print("TEST...")
print("")

print("Testing scalar...")
time.sleep(0.25)
def function(x):
    return x*x-4

def deri(x):
    return 2*x

def function2(x):
    return x**3-x**2
    
def deri2(x):
    return 3*x**2-2*x

start,eps,N=-1.0,0.01,100
eps2=0.01
print("Solution de la fonction f:x-> x**2 - 4 avec U0="+str(start)+" epsilon = "+str(eps)+" : "+str(Newton_Raphson(function,deri,start,N,eps)))
print("Solution de la fonction f:x-> x**3-x**2 avec U0="+str(start)+" epsilon = "+str(eps)+" : "+str(Newton_Raphson(function2,deri2,start,N,eps)))

time.sleep(0.25)
print("")

print("Testing matrixes...")
print("")
def f_mat_1(X):
    return ((X[0]+X[1])/2,(X[0]-X[1])/2)


Jacobian=np.zeros((2,2))
Jacobian[0][1]=1
Jacobian[0][0]=1
Jacobian[1][0]=1
Jacobian[1][1]=-1

print("Solving f(u,v)-> ((u+v)/2,(u-v)/2)=(0,0),where jacobian matrix  of f is ")
print(Jacobian,)
print("starting point : [1,1]")
start_mat=np.ones(2)
print(Newton_Raphson(f_mat_1,Jacobian,start_mat,100,eps))


#print("Solution :"+str(Newton_Raphson()))



#QUESTION 4

#print("Solution de la fonction f:x-> x**2 avec U0=",start,"epsilon = ",epsilon," : ","epsilon2 ( bactracking) = ",Newton_Raphson_backtrack(function,deri,start,N,eps,eps2))
#print("Solution de la fonction f:x-> x**3-x**2 avec U0=",start,"epsilon = ",epsilon,"epsilon2 ( bactracking) = ",eps2," : ",Newton_Raphson_backtrack(function2,deri2,start,eps,eps2))

