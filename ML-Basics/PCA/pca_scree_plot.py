import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA

# Load dataset
iris = datasets.load_iris()
X = iris.data

# Apply PCA
pca = PCA()
pca.fit(X)

# explained variance
explained_var = pca.explained_variance_ratio_

# Scree plot
plt.plot(range(1, len(explained_var) + 1), explained_var, 'o-', linewidth=2)
plt.title("Scree Plot (Explained Variance per Component)")
plt.xlabel("Principal Component")
plt.ylabel("Explained Variance Ratio")
plt.grid(True)
plt.show()