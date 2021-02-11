"""Problem 1 in Homework set 3 for ASTR260"""
#finished by Kay Towner

import math
import numpy as np
#import ipdb

def f(x):
    """function to test in our derivative
    program"""
    return x**3 - 5*x + 2

def analytic_deriv_f(x):
    """The analytic derivative of
     x**3 - 5*x + 2."""
    ###FILL THIS IN WITH CODE
    
    return 3*x**2-5

def absolute_error(truth, computed):
    """returns the absolute error between
    the computed and true value"""
    return np.abs(truth-computed)

def relative_error(truth, computed):
    """returns the relative error between
    the computed and true value"""
    ###FILL THIS IN WITH CODE
    
    return (analytical_deriv_f(x) - absolute_error(truth, computed))/(absolute_error(truth, computed))

def forward_difference(x, h, func=None):
    """Computes the numerical derivative
    of an arbitrary function using the forward
    difference method.
    x: point at which to evaluate the func
    h: stepsize to compute the secant
    func: a valid python function"""
    numerator = func(x+h)-func(x)
    denominator = h
    return numerator/denominator

def central_difference(x, h, func=None):
    """Computes the numerical derivative
    of an arbitrary function using the central
    difference method.
    x: point at which to evaluate the func
    h: stepsize to compute the secant
    func: a valid python function"""
    ###FILL THIS IN WITH CODE
    numerator = func(x+h)-func(x-h)
    denominator = 2*h  
    return numerator/denominator

if __name__ == "__main__":
    print("The central difference of x**3 - 5*x + 2,"+
          " evaluated at 0, with stepsize 0.01, is:")
    print(str(forward_difference(0, 0.01, f)))

    print("Generating data for part 1 of problem 1")
    #Data for part 1, over the range -5-->5
    output_data_fullrange = []
    h = 0.01
    #loop over an array from -5 to 5  in steps of 0.01
    for x_val in np.arange(-5, 5, h):
        #calculate analytic derivative, fw diff, and central diff
        analytic_diff = analytic_deriv_f(x_val)
        fw_diff = forward_difference(x_val, h, f)
        central_diff = central_difference(x_val, h, f)
        #store this as a tuple        
        data = (x_val, analytic_diff, \
                fw_diff, central_diff)
        #append this to a list        
        output_data_fullrange.append(data)

    #save this as an output textfile for plotting
    fname_part1 = 'problem_1_1_data.txt'
    np.savetxt(fname_part1, #filename
               np.array(output_data_fullrange), #data to save
               delimiter=',', #how to separate values in the file
               header=("function: x**3-5x+3\n"+
               "x, analytic_deriv(x), fw_diff(x), central_diff(x)"),
               fmt = '%.05f')#<--5 digits of precision, look up "format codes"
    print("Saved data to: "+fname_part1+"\n\n")

    print("Generating data for part 2 of problem 1")
    #now you do the rest...

    #calculat the error with forward. pic values of h error at x = 0
    #pic values of h: .00, .001 ect. .
    #use func to generate values
    
    truth = analytic_deriv_f(0)
    h = [.00, .001, .002, .003]











