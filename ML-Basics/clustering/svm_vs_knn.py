"""
Comparison of SVM and k-NN on Iris dataset
- Trains both classifiers
- Prints accuracies
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# Load dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train SVM
svm = SVC(kernel='rbf', gamma='scale', C=1.0)
svm.fit(X_train, y_train)
print("SVM Accuracy:", svm.score(X_test, y_test))

# Train k-NN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
print("k-NN Accuracy:", knn.score(X_test, y_test))
