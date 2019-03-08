from math import pi, pow, tan, atan#Import Math functions

def sin_p(theta:float, p:float):
    """
    Sine-function for any l^p metric with a p >= 1 and p < inf.
    Raises an Exception if the p is smaller than 1.  
    """
    if p < 1: raise Exception("p must be >= 1")#Raise an Exception if p is too low
    while theta > 2*pi: theta -= 2 * pi #get theta between 0 and 2*pi
    while theta < 0:  theta += 2 * pi #get theta between 0 and 2*pi
    if theta <= pi: return abs(tan(theta))/pow(1 + pow(abs(tan(theta)), p), 1/p)
    else: return -abs(tan(theta))/pow(1 + pow( abs(tan(theta)), p), 1/p)

def cos_p(theta:float, p:float):
    """
    Cosine-function for any l^p metric with a p >= 1 and p < inf.
    Raises an Exception if the p is smaller than 1.  
    """
    if p < 1: raise Exception("p must be >= 1")#Raise an Exception if p is too low
    while theta > 2*pi: theta -= 2 * pi #get theta between 0 and 2*pi
    while theta < 0:  theta += 2 * pi #get theta between 0 and 2*pi
    if theta <= 0.5 * pi or theta >= 1.5 * pi: return 1/pow(1 + pow(abs(tan(theta)), p), 1/p)
    else: return -1/pow(1 + pow(abs(tan(theta)), p), 1/p)

def sin_chebyshev(theta:float):
    """
    Sine-function in the Chebyshev-metric.
    """
    while theta > 2*pi: theta -= 2 * pi #get theta between 0 and 2*pi
    while theta < 0:  theta += 2 * pi #get theta between 0 and 2*pi
    if -pi/4 <= theta and theta < pi/4: return tan(theta)
    elif pi/4 <= theta and theta <= pi * 0.75: return 1
    elif pi * 0.75 < theta and theta < 1.25 * pi: return - tan(theta)
    elif theta <= 1.75 * pi: return -1
    else: return tan(theta)

def cos_chebyshev(theta:float):
    """
    Cosine-function in the Chebyshev-metric.
    """
    while theta > 2*pi: theta -= 2 * pi #get theta between 0 and 2*pi
    while theta < 0:  theta += 2 * pi #get theta between 0 and 2*pi
    if -pi/4 <= theta and theta < pi/4: return 1
    elif pi/4 <= theta and theta <= pi * 0.75: return -tan(theta - 0.5*pi)
    elif pi * 0.75 < theta and theta < 1.25 * pi: return -1
    elif theta <= 1.75 * pi: return tan(theta - 0.5*pi)
    else: return 1

def ratio(theta:float, p1:float, p2:float):# Get the Ratio between the triangles inside the resepctive unit circles for some angle theta
    if p1 < 1 or p2 < 1: raise Exception("p1 and p2 must be >= 1") #Raise an Exception if p is too low
    return pow(abs(pow(sin_p(theta, p2), p1)) + abs(pow(cos_p(theta, p2), p1)), 1/p1)

def get_angle(x, y): #get the angle of the vector from the origin the point (x,y)
    if x == 0: return (y==1)*0.5*pi + (y==-1)*1.5*pi
    else: return atan(y/x)
    