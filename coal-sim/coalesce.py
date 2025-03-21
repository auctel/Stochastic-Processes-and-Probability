
import numpy as np
import matplotlib.pyplot as plt


###########################################################################
#                                                                         #
#     Simulates a simple Kingman coalescent process for a                 #
#     given population size N and an initial number of lineages.          #
#                                                                         #
###########################################################################

def coalescent_simulation(N, num_lineages):

    time = 0
    times = [0]
    lineages = num_lineages
    lineage_counts = [lineages]
    
    while lineages > 1:
        rate = lineages * (lineages - 1) / (2 * N) 
        wait_time = np.random.exponential(1 / rate)
        time += wait_time
        lineages -= 1
        times.append(time)
        lineage_counts.append(lineages)
    
    return times, lineage_counts

def plot_coalescence(times, lineage_counts):
    plt.step(times, lineage_counts, where='post')
    plt.xlabel("Time")
    plt.ylabel("Number of Lineages")
    plt.title("Coalescence Simulation")
    plt.show()

# run with these parameters
N = 1000  # pop
num_lineages = 10  # sample
times, lineage_counts = coalescent_simulation(N, num_lineages)
plot_coalescence(times, lineage_counts)
