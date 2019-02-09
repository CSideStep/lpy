from Core.trig import *
import matplotlib.pyplot as plt
from typing import List

ASVECTORFIELD=0
ASFUNCTION=1
ASVECTORSONCIRCLE=2

def plot_function(f, min_x:float, max_x:float, steps:int=100):
    """
    This function plots a function, using matploblib, for some interval with a given numbers of calculated steps.
    f is some function, which takes a real number from the interval and returns another real number.
    """
    xs = [min_x + (max_x-min_x)*i/(steps-1) for i in range(steps)] #generate the x-values and store them in a list
    ys = [f(x) for x in xs] #generate the y-values and store them in a list
    plt.plot(xs, ys) #generagte the plot based of the lists
    plt.show() #show the plot

def plot_vector_field(xs:List[float], ys:List[float], us:List[float], vs:List[float]):
    """
    This functions plots a vector field using matplotlib. Just a helper-function to reduce redundant code. 
    """    
    plt.quiver(xs, ys, us, vs) #generate the plot
    plt.show() # display the plot

def display_transformation(p1:float, p2:float, mode:int=ASVECTORFIELD, resolution:int=10):
    """
    This function display the difference between two metrics as a vector field,
    a function or as a bunch of vectors on the unit circle.
    """
    if mode==ASVECTORFIELD: #Display a vectorfield
        xs,ys,us,vs = [], [], [], []
        for x in range(resolution):
            for y in range(resolution):
                cx=x-(resolution-1)/2
                cy=y-(resolution-1)/2
                xs.append(cx)
                ys.append(cy)
                theta = get_angle(cx, cy)
                us.append(cx*ratio(theta, p1, p2)-cx)
                vs.append(cy*ratio(theta, p1, p2)-cy)
        plot_vector_field(xs, ys, us, vs)
    elif mode==ASVECTORSONCIRCLE: #Display vectors on the unitcircle of the first metric
        xs,ys,us,vs = [], [], [], []
        for i in range(resolution**2):
            theta = 2*pi*i/(-1+resolution**2)
            cx = cos_p(theta, p1)
            cy = sin_p(theta, p1)
            xs.append(cx)
            ys.append(cy)
            us.append(cos_p(theta, p2)-cx) 
            vs.append(sin_p(theta, p2)-cy)
        plot_vector_field(xs, ys, us, vs)
    elif mode==ASFUNCTION: #plot the Ratio function
        plot_function(lambda x:float: ratio(x, p1, p2), 0, 2*pi, steps=resolution**2)
        