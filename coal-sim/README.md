# coalesce.py

## Introduction
The provided Python code simulates a simple coalescence process using the Kingman coalescent model, which is a fundamental concept in population genetics. This model describes the genealogical relationships of alleles in a population by tracing their ancestry back in time until a common ancestor is found.

## Overview of the Code
The code consists of two primary functions:

1. `coalescent_simulation(N, num_lineages)`: This function simulates the coalescence process given a population size (`N`) and an initial number of sampled lineages (`num_lineages`).
2. `plot_coalescence(times, lineage_counts)`: This function visualizes the coalescence process by plotting the number of lineages over time.

## Coalescence Process
The simulation follows these steps:
- Start with a given number of sampled lineages.
- At each step, two lineages coalesce at a rate determined by the formula:
  
rate = k(k-1) / (2N)
  
  where \( k \) is the number of current lineages, and \( N \) is the population size.
- The time until the next coalescence event is drawn from an exponential distribution with the inverse of the coalescence rate as the mean.
- The number of lineages decreases by one, and the process repeats until only a single lineage remains.

## Visualization
The `plot_coalescence` function generates a step plot showing how the number of lineages decreases over time due to coalescence events.

## Example Execution
To run the simulation with a population size of 1000 and an initial sample of 10 lineages:
```python
N = 1000  # Population size
num_lineages = 10  # Initial sample size
times, lineage_counts = coalescent_simulation(N, num_lineages)
plot_coalescence(times, lineage_counts)
```
This will produce a plot illustrating the coalescence process over time.

## Conclusion
This simulation provides a simple yet effective way to visualize the Kingman coalescent, which is widely used in population genetics to model the ancestry of genetic samples. The exponential waiting times between coalescence events reflect the stochastic nature of genetic ancestry in finite populations.


# Coalescence Animation coal_animation.py

The animation visualizes the Kingman coalescent process, where an initial set of sampled lineages progressively merge backward in time until they converge to a single common ancestor. Each merging event represents a genetic coalescence, occurring at a rate dependent on population size, with more recent events happening quickly and deeper coalescence taking longer.