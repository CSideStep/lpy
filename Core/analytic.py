from functools import reduce
from math import pi
from Core.trig import sin_p, cos_p
def approx_integrate(f, x_min:float, x_max:float, steps:int=1000, over_approx:bool=False):
    """
    Approx the area under f in some intervall (x_min, x_max)
    """
    xs=[x_min+(x_max-x_min)*i/(steps-1) for i in range(steps)]
    scaled_ys=[f(x)*((x_max-x_min)/(steps + (-1*over_approx))) for x in xs]
    return sum(scaled_ys)

def approx_diff(f, x:float, offset:float=0.001):
    """
    Approx. the slope of the tangent of f at x
    """
    return (f(x+offset) - f(x))/offset

def approx_pi(p:float, steps=1000):
    """
    Approx pi in any l^p metric
    """
    return 2*approx_integrate(lambda x: pow(pow(abs(approx_diff(lambda x: cos_p(x, p), x)), p) 
                                        + pow(abs(approx_diff(lambda x: sin_p(x, p), x)), p), 1/p), 0, 0.5*pi)