# Categorize crime levels and compute unemployment

import pandas as pd

# Load the dataset
df = pd.read_csv("crime.csv")

# Create risk column based on ViolentCrimesPerPop
df['risk'] = df['ViolentCrimesPerPop'].apply(lambda x: 'HighCrime' if x >= 0.50 else 'LowCrime')

# Group by risk and calculate average unemployment
avg_unemployment = df.groupby('risk')['PctUnemployed'].mean().round(3)

# Print results in a clear format
for risk_level, avg_rate in avg_unemployment.items():
    print(f"Average unemployment rate for {risk_level}: {avg_rate}")