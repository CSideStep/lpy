from Core.trig import ratio, sin_p, cos_p, get_angle
from Core.visual import display_transformation, ASVECTORSONCIRCLE, ASVECTORFIELD, display_pi_of_p, plot_function
from math import pi, sin, factorial
from Core.numeric import approx_integrate, approx_diff, approx_pi

if __name__ == "__main__":
    min_p=1
    max_p=20
    steps=50000
    increment=(max_p-min_p)/steps
    with open("pi.csv", "w+") as f:
        for i in range(steps):
            p=min_p + i * increment
            f.write(str(p) +","+str(approx_pi(p))+ "\n")
        