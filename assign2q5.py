# Create grade bands and summary table

import pandas as pd

df = pd.read_csv("student.csv")

# Create the grade_band column
def grade_band(grade):
    if grade <= 9:
        return "Low"
    elif 10 <= grade <= 14:
        return "Medium"
    else:  # grade >= 15
        return "High"

df['grade_band'] = df['grade'].apply(grade_band)

# Group by grade_band and summarize
summary = df.groupby('grade_band').agg(
    num_students=('grade', 'count'),
    avg_absences=('absences', 'mean'),
    pct_internet=('internet', lambda x: (x.sum() / len(x)) * 100)
).reset_index()

# Round numeric columns
summary['avg_absences'] = summary['avg_absences'].round(2)
summary['pct_internet'] = summary['pct_internet'].round(2)

summary.to_csv("student_bands.csv", index=False)

print(summary)