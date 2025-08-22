import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Load dataset
iris = datasets.load_iris()
X = iris.data  # 4 features
y = iris.target
target_names = iris.target_names

# apply pca (reduce to 2D)
pca = PCA(n_components=2)
X_r = pca.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_r, y, test_size=0.2, random_state=42)

# train SVM
clf = SVC(kernel="linear")
clf.fit(X_train, y_train)


print("SVM Accuracy on PCA-reduced data:", clf.score(X_test, y_test))
