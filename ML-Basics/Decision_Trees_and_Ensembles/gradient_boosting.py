"""
Gradient Boosting Classifier Example
- Uses scikit-learn's GradientBoostingClassifier on the Iris dataset
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize Gradient Boosting Classifier
gb_clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

# Train model
gb_clf.fit(X_train, y_train)

# Evaluate accuracy
gb_accuracy = gb_clf.score(X_test, y_test)
print(f"Gradient Boosting Accuracy: {gb_accuracy:.2f}")
