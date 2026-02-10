# Compute basic statistics for ViolentCrimesPerPop

import pandas as pd

df = pd.read_csv("crime.csv")

crime_rates = df["ViolentCrimesPerPop"]

# Compute statistics
mean_val = crime_rates.mean()
median_val = crime_rates.median()
std_val = crime_rates.std()
min_val = crime_rates.min()
max_val = crime_rates.max()

# Print results
print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_val)
print("Minimum:", min_val)
print("Maximum:", max_val)

# The mean is compared to the median to understand the shape of the distribution.
# Since the mean is larger than the median, the data is right-skewed.
# The maximum value 1.0 is much higher than most values, indicating an extreme value;
# such extremes affect the mean more than the median.