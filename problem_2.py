"""Problem 2 from Hwk 3 of ASTR260"""
#finished by Kay Towner

import numpy as np
import matplotlib.pyplot as plt

def f(t):
    """function to test in our derivative
    program"""
    return (1) * sin(2*pi* (0.02) * t)

def analytic_deriv_f(t):
    """The analytic derivative of
     x**3 - 5*x + 2."""
    return cos(2*pi* (0.02) * t) * (2*pi*(0.02))

def absolute_error(truth, computed):
    """returns the absolute error between
    the computed and true value"""
    return np.abs(truth-computed)

def relative_error(truth, computed):
    """returns the relative error between
    the computed and true value"""
    return (analytical_deriv_f(t) - absolute_error(truth, computed))/(absolute_error(truth, computed))

def forward_difference(t, h, func=None):
    """Computes the numerical derivative
    of an arbitrary function using the forward
    difference method.
    x: point at which to evaluate the func
    h: stepsize to compute the secant
    func: a valid python function"""
    numerator = func(t+h)-func(t)
    denominator = h
    return numerator/denominator

def central_difference(x, h, func=None):
    """Computes the numerical derivative
    of an arbitrary function using the central
    difference method.
    x: point at which to evaluate the func
    h: stepsize to compute the secant
    func: a valid python function"""
    numerator = func(x+h)-func(x-h)
    denominator = 2*h  
    return numerator/denominator


if __name__ == "__main__":
    path_to_data = "/Users/K A Y/Desktop/astro160labs/sensor_position_data.txt"
    oscillator_data = np.loadtxt(path_to_data, skiprows=1, delimiter=',')
    #pulls out the first column (remember things start at 0 in python)
    oscillator_time = oscillator_data[:,0]
    oscillator_pos  = oscillator_data[:,1]

    plt.plot(oscillator_time, oscillator_pos)
    plt.show()
    
