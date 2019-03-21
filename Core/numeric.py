from functools import reduce
from math import pi, factorial
from Core.trig import sin_p, cos_p

def approx_integrate(f, x_min:float, x_max:float, steps:int=1000):
    """
    Approx the area under f in some intervall (x_min, x_max)
    """
    xs=[x_min+(x_max-x_min)*(i)/(steps) for i in range(steps)] #get xs
    scaled_ys=[f(x)*((x_max-x_min)/(steps)) for x in xs] #f(x) * width, for every x
    return sum(scaled_ys) #return the sum

def approx_diff(f, x:float, offset:float=0.01):
    """
    Approx. the slope of the tangent of f at x
    """
    return (f(x+offset/2) - f(x-offset/2))/offset #df/dx

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

def save_pi_csv(path="pi.csv", min_p:float=1, max_p:float=80, steps:int=50):
    increment=(max_p-min_p)/steps#calculate stepsize
    with open(path, "w+") as f: #open the file
        for i in range(steps): #for each step
            p=min_p + i * increment #calculate p
            f.write(str(p) +","+str(approx_pi(p))+ "\n") #calculate pi(p), write p, pi(p) at the end of the csv.