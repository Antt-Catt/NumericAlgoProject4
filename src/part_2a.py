import numpy as np

#def f_elast():

def f_centri(x0, y0, k):
    return lambda x, y : np.array([k * (x - x0), k * (y - y0)])

def f_gravi(x0, y0, k):
    return lambda x, y : np.array([-k*(x-x0)/(((x-x0)**2+(y-y0)**2)**(3/2)),-k*(y-y0)/(((x-x0)**2+(y-y0)**2)**(3/2))])

print(f_centri(2, 6, 7)(4, 3))
print(f_gravi(2, 6, 7)(4, 3))
