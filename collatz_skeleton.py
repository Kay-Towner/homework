import numpy as np

def number_of_steps_to_one(number):
    """Function which determines how many steps
    it takes for a number to reach 1 in the Collatz
    sequence
    input: number (a positive integer)
    output: steps 
    """
    if not isinstance(number, int):
        raise ValueError("number must be integer")
    if not number>1:
        raise ValueError("number must be larger than one")
    #Fill this in with an algorithm that calculates
    #the number of steps needed to reach one
    while number > 1:
        steps = steps + 1
    
    return steps


def collatz_func(number):
    """Function preforms either division or multiplication on the number
    based on if the number is even or odd.
    input: a number
    output: a number either even/odd
    """
    if is_even(number) == True:
        return number/2
    else:
        return 3 * number + 1

def is_even(number):
    """Funtion runs a true/false statement on the number.
    input: a number
    output: either zero = true or false otherwise
    """
    if number % 2 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    max_number_to_check = 10**5
    numbers_to_check = np.
    #Fill this section in 
    #write a for loop that iterates from 1 -> max_number to check
    #and calculates the number of steps to get to 1
    """For loop that looks at the ranges 1 to the max#
    """
    for number_of_steps_to_one in range(1, max_number_to_check):
        print(steps)

        f = open('collatz_output.txt', 'w')

    





















