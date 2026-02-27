import statistics as st

"""
Python statistics Module
Provides functions for calculating mathematical statistics of numeric data.
"""

data = [1, 2, 3, 4, 4, 4, 5, 6, 100]

print(f"Data: {data}")

print("\n--- Averages and Central Tendency ---")
print(f"Mean: {st.mean(data)}")
print(f"Median: {st.median(data)}")
print(f"Mode: {st.mode(data)}")
print(f"Geometric Mean: {st.geometric_mean([1, 10, 100])}")
print(f"Harmonic Mean: {st.harmonic_mean([40, 60])}")

print("\n--- Measures of Spread ---")
print(f"Variance: {st.variance(data)}")
print(f"Standard Deviation: {st.stdev(data)}")
print(f"Population Variance: {st.pvariance(data)}")
print(f"Population Standard Deviation: {st.pstdev(data)}")

print("\n--- Statistical Analysis ---")
print(f"Quantiles: {st.quantiles(data, n=4)}") # quartiles by default
