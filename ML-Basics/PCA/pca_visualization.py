import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA

# Load dataset
iris = datasets.load_iris()
X = iris.data  # 4 features
y = iris.target
target_names = iris.target_names

# apply pca (reduce to 2D)
pca = PCA(n_components=2)
X_r = pca.fit_transform(X)

# Explained variance ratio (how much info kept in each PC)
print("Explained variance ratio:", pca.explained_variance_ratio_)

# Plot
plt.figure()
colors = ['navy', 'turquoise', 'darkorange']
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], alpha=.7, color=color,
                label=target_name)

plt.legend()
plt.title("PCA of Iris dataset (2D projection)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(True)
plt.show()