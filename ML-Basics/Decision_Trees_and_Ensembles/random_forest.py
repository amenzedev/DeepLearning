"""
Random Forest Classifier Example
- Uses scikit-learn's RandomForestClassifier on the Iris dataset
- Compares performance with a single decision tree
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# load dataset
iris = load_iris()
X, y = iris.data, iris.target

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# initilize RFC
rf_clf = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42)

# train model
rf_clf.fit(X_train, y_train)

# evaluate accuracy
rf_accuracy = rf_clf.score(X_test, y_test)
print(f"Random Forest Accuracy: {rf_accuracy:.2f}")

# Feature importance
importances = rf_clf.feature_importances_
for name, importance in zip(iris.feature_names, importances):
    print(f"{name}: {importance:.3f}")