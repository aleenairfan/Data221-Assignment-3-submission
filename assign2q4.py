# Filter students by study time, internet, and absences

import pandas as pd

df = pd.read_csv("student.csv")

# Filter students
filtered = df[
    (df['studytime'] >= 3) &
    (df['internet'] == 1) &
    (df['absences'] <= 5)
]

filtered.to_csv("high_engagement.csv", index=False)

# Compute stats
num_students = len(filtered)
avg_grade = filtered['grade'].mean()

print(f"Number of students saved: {num_students}")
print(f"Average grade: {avg_grade:.2f}")