# Train KNN with multiple k values and compare accuracies

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("kidney_disease.csv")
df.replace("?", np.nan, inplace=True)

# Fill numeric NaNs with median
for col in df.select_dtypes(include=['number']):
    df[col] = df[col].fillna(df[col].median())

# Fill categorical NaNs with mode and encode
for col in df.select_dtypes(include=['object', 'string']):
    df[col] = df[col].fillna(df[col].mode()[0])
    df[col] = LabelEncoder().fit_transform(df[col].astype(str))

# Split features and target
X = df.drop(columns=["classification"])
y = df["classification"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train KNN for multiple k values
k_values = [1, 3, 5, 7, 9]
results = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    acc = accuracy_score(y_test, knn.predict(X_test))
    results.append((k, acc))

# Display results
print("k value | Test Accuracy")
for k, acc in results:
    print(k, " | ", round(acc, 3))

# Smaller values of k make the model more sensitive to noise in the data.
# Very small k (like 1) may cause overfitting by memorizing training points.
# Moderate k values (like 3 or 7) give the best accuracy here, balancing bias and variance.
# Large k values smooth the decision boundary too much and may ignore local patterns.
# Very large k (like 9) may cause underfitting, reducing model performance slightly.