from functools import reduce
from math import pi
import Core.visual as v
from Core.trig import sin_p, cos_p

def approx_integrate(f, x_min:float, x_max:float, steps:int=1000, right_focus:bool=False):
    """
    Approx the area under f in some intervall (x_min, x_max)
    """
    xs=[x_min+(x_max-x_min)*(i+right_focus)/(steps-right_focus) for i in range(steps)] #get xs
    scaled_ys=[f(x)*((x_max-x_min)/(steps)) for x in xs] #f(x) * width, for every x
    return sum(scaled_ys) #return the sum

def approx_diff(f, x:float, offset:float=0.001):
    """
    Approx. the slope of the tangent of f at x
    """
    return (f(x+offset) - f(x))/offset #df/dx

def approx_pi(p:float, steps=1000, chebyshev=False):
    """
    Approx pi in any l^p metric
    """
    if chebyshev: return 4
    else : return 2*approx_integrate( # two times a quarter to get half a circle = pi
                              lambda x: pow(
                                        pow(abs(approx_diff(lambda x: cos_p(x, p), x)), p) #|(dx/dtheta)|^p
                                        + pow(abs(approx_diff(lambda x: sin_p(x, p), x)), p), #|(dy/dtheta)|^p
                                        1/p), # sum^(1/p) 
                              0, 0.5*pi) #integrate from 0 to 0.5 pi, to get one-forth of circle