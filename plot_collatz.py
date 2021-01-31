import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    inputfile = 'collatz_output.txt'
    data = np.genfromtxt(open('collatz_output.txt'), dtype=np.int, 
                         skip_header=1)
    print(data)

x = [data.split()[0]]
y = [data.split()[1]]

plt.plot(x, y)
plt.show()
