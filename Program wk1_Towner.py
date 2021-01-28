import matplotlib.pyplot as plt
import numpy as np
import math


#part 1.
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

    length = steps
    step_counter = number +1

    f = open("stepfile.txt", 'a')
    f.write(steps)
    f.close()
    
    return steps

if __name__ == "__main__":
    max_number_to_check = 10**5
    numbers_to_check = np.append()
    #Fill this section in 
    #write a for loop that iterates from 1 -> max_number to check
    #and calculates the number of steps to get to 1
    for number in range(1, max_number):
        print(number)
    for steps in numbers_to_check:
        print(len(steps))

#part 2.
        
if __name__ == "__main__":
    inputfile = 'collatz_output.txt'
    data = np.genfromtxt(open('collatz_output.txt'), dtype=np.int, 
                         skip_header=1)
    print(data)

#plot n vs L(n) for ranges:

#x
n = number
#y
Ln = length

pyplot.hist(n, label='number')
pyplot.hist(Ln, label='steps taken')

axs[0, 0].plot(n, Ln, 'tab:red')
axs[0, 0].set_title('n = 100')

axs[0, 1].plot(n, Ln, 'tab:orange')
axs[0, 1].set_title('n = 1000')

axs[1, 0].plot(n, Ln), 'tab:green')
axs[1, 0].set_title('n = 10000')

for ax in axs.flat:
    ax.set(xlabel='number', ylabel='Length of number')
    
for ax in axs.flat:
    ax.label_outer()

plt.savefig('NumberGraph.png')















    
