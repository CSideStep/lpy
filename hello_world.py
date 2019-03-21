from Core.trig import ratio, sin_p, cos_p, get_angle
from Core.visual import display_transformation, ASVECTORSONCIRCLE, ASVECTORFIELD, display_pi_of_p, plot_function
from math import pi, sin, factorial, tan
from Core.numeric import approx_integrate, approx_diff, approx_pi, save_pi_csv

if __name__ == "__main__":
    print(approx_integrate(lambda x: x**2, 0, 2))
        