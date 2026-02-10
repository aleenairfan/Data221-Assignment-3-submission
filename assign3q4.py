# Train KNN on kidney data and evaluate with metrics

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import LabelEncoder

# Load data and replace special missing values
df = pd.read_csv("kidney_disease.csv")
df.replace('?', np.nan, inplace=True)

# Fill numeric columns with median
for col in df.select_dtypes(include=['number']):
    df[col] = df[col].fillna(df[col].median())

# Fill categorical columns with mode and encode
for col in df.select_dtypes(include=['object', 'string']):
    df[col] = df[col].fillna(df[col].mode()[0])
    df[col] = LabelEncoder().fit_transform(df[col].astype(str))

# Map target labels from [0,2] → [0,1] for convenience
df['classification'] = df['classification'].replace({0:0, 2:1})

# Features and target
X = df.drop(columns=['classification'])
y = df['classification']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# Metrics
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1-score:", f1_score(y_test, y_pred))

# True Positives: patients correctly predicted to have kidney disease
# True Negatives: healthy patients correctly predicted as healthy
# False Positives: healthy patients incorrectly predicted as having disease
# False Negatives: sick patients incorrectly predicted as healthy
# Accuracy can be misleading if classes are imbalanced
# Recall is most important if missing a kidney disease case is serious