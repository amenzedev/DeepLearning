"""
Decision Tree Classifier Example
- Uses scikit-learn's DecisionTreeClassifier on the Iris dataset
- Visualizes the tree
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# load dataset
iris = load_iris()
X, y = iris.data, iris.target

# split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# initialize DTC
clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)

# trail model
clf.fit(X_train, y_train)

# evaluate accuracy
accuracy = clf.score(X_test, y_test)
print(f"Decision Tree Accuracy: {accuracy:.2f}")

# Visualize the tree
plt.figure(figsize=(10, 6))
plot_tree(clf, feature_names=iris.feature_names, class_names=list(iris.target_names), filled=True)
plt.title("Decision Tree Classifier (Iris Dataset)")
plt.show()