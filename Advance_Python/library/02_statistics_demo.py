import statistics

"""
Python statistics Module
Provides functions for calculating mathematical statistics of numeric data.
"""

data = [1, 2, 3, 4, 4, 4, 5, 6, 100]

print(f"Data: {data}")

print("\n--- Averages and Central Tendency ---")
print(f"Mean: {statistics.mean(data)}")
print(f"Median: {statistics.median(data)}")
print(f"Mode: {statistics.mode(data)}")
print(f"Geometric Mean: {statistics.geometric_mean([1, 10, 100])}")
print(f"Harmonic Mean: {statistics.harmonic_mean([40, 60])}")

print("\n--- Measures of Spread ---")
print(f"Variance: {statistics.variance(data)}")
print(f"Standard Deviation: {statistics.stdev(data)}")
print(f"Population Variance: {statistics.pvariance(data)}")
print(f"Population Standard Deviation: {statistics.pstdev(data)}")

print("\n--- Statistical Analysis ---")
print(f"Quantiles: {statistics.quantiles(data, n=4)}") # quartiles by default
