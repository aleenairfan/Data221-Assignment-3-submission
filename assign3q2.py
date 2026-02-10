# Create histogram and box plot for ViolentCrimesPerPop

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("crime.csv")
crime_rates = df["ViolentCrimesPerPop"]

# Histogram
plt.figure()
plt.hist(crime_rates)
plt.title("Histogram of Violent Crimes Per Population")
plt.xlabel("ViolentCrimesPerPop")
plt.ylabel("Frequency")
plt.show()

# Box plot
plt.figure()
plt.boxplot(crime_rates)
plt.title("Box Plot of Violent Crimes Per Population")
plt.xlabel("ViolentCrimesPerPop")
plt.ylabel("Values")
plt.show()

# The histogram shows that values from 0.0 to 0.7 have frequencies above 30, while values from 0.7 to 1.0 occur less frequently.
# Most communities have lower crime rates, with fewer communities having very high crime rates, indicating a right-skewed distribution.
# The box plot shows the median at 0.4, the lower quartile around 0.2, and the upper quartile around 0.7.
# The box spans from the minimum 0.02 to the maximum 1.0, showing the full range of the data.
# Since there are no points beyond the whiskers, the box plot suggests there are no extreme outliers in this dataset.