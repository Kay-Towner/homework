import matplotlib.pyplot as plt
import numpy as np

#finished by Kay Towner

if __name__ == "__main__":
    fname_part1 = 'problem_1_1_data.txt'
    data_to_plot = np.loadtxt(fname_part1,
                              delimiter=',',
                              skiprows=2)
    print("Data to plot:")
    print(data_to_plot)
    #now you make the plot and save it.

    plt.plot(data_to_plot)
    plt.yscale("log")
    plt.show()
    plt.savefig('Homework_3graph.png')
