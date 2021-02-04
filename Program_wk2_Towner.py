import numpy as py
import math

#1.

#the constants:
a_1= 15.8
a_2= 18.3
a_3= 0.714
a_4= 23.2
a_5= a5(A, Z)


def func_for_afive(A, Z):
    """Function to find the value of a_5
    input: A and Z
    output: a number based upon odd or even inputs
    """
    if odd_even_calc(A) == False:
        return 0
    if odd_even_calc(A, Z) == True:
        return 12.0
    if odd_even_calc(A) == True and odd_even(Z) == False:
        return -12.0

def a5(A, Z):
    """Funtion runs a true/false statement on the number.
    input: a number: A and Z
    output: either zero = true or false otherwise
    """
    if A % 2 == 0:
        if Z % 2 == 0:
            return 12.0
        else:
            return -12.0


def odd_even_calc(A, Z):
    """Function to calculate the odd and evens for the
    A and Z numbers
    input: a number
    output: an odd/ even test outcome for A and Z
    """
    if A % 2 == 0:
        return True
    else:
        return False
    if Z % 2 == 0:
        return True
    else:
        return False

#the section where I make the long equation nicer and less scary
""" Input numbers for A and Z """
A= 58
Z= 28
B= j - k - L - m + n

print(B)

def binding_energy(A, Z):
    return (a_1)*A-(a_2)*(A**(2/3))-(a_3)*((Z**2)/(A**(1/3))- (a_4)*(((A-(2*Z))**2)/(A)-(a_5)/A**(1/2)

#c.
def bad_float_compare(A, Z):
    """Function to see if two numbers are equal
    input:
    output: returns true if equal
    """
    if A == Z:
        return True
    
def good_float_compare(A, Z):
    """A function to correctly work the assert test case.
    """
    if 








#helpful notes from Lab:
##"""to generate the output run this program"""
##def coulomb_term(a,z):
##    return true
##
##def volume_term(a,z):
##    return true
##
##def binding_energy(a,z):
##    return coulomb_term(a,z) + volume_term(a,z)
##
##
##
##def bad_float_compare():
##
##
##A == B
##A != B
##
###five to the 2/3 power:  5**(2/3)
