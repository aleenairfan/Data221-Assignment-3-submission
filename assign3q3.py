# Split kidney disease dataset into training and testing sets

import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("kidney_disease.csv")

# Feature matrix and label vector
X = df.drop(columns=["classification"])
y = df["classification"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# We should not train and test on the same data because the model
# would memorize the data and not generalize well.
# The testing set is used to evaluate how well the model performs
# on unseen data, which reflects real-world performance.