import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression, make_classification
import numpy as np

# =========================================================
# 2️⃣ MULTI-CLASS LOGISTIC REGRESSION
# =========================================================

# --- Create synthetic classification dataset ---
X_clf_np, y_clf_np = make_classification(
    n_samples=300, n_features=2, n_classes=3, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=42
)
X_clf = torch.tensor(X_clf_np, dtype=torch.float32)
y_clf = torch.tensor(y_clf_np, dtype=torch.long)  # For multi-class, labels must be long

# --- Define multi-class logistic regression model ---
model_clf = nn.Linear(2, 3)  # 2 input features → 3 output classes

# --- Loss & optimizer ---
loss_fn_clf = nn.CrossEntropyLoss()  # Softmax + Cross-Entropy combined
optimizer_clf = torch.optim.SGD(model_clf.parameters(), lr=0.1)

# --- Training loop ---
for epoch in range(300):
    y_logits = model_clf(X_clf)           # Raw scores for each class
    loss = loss_fn_clf(y_logits, y_clf)   # Cross-entropy loss

    optimizer_clf.zero_grad()
    loss.backward()
    optimizer_clf.step()

print("Multi-class Logistic Regression Weights:\n", model_clf.weight.data.numpy())
print("Multi-class Logistic Regression Bias:\n", model_clf.bias.data.numpy())

# --- Plot decision boundaries ---
with torch.no_grad():
    x_min, x_max = X_clf_np[:, 0].min() - 1, X_clf_np[:, 0].max() + 1
    y_min, y_max = X_clf_np[:, 1].min() - 1, X_clf_np[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))

    grid = torch.tensor(np.c_[xx.ravel(), yy.ravel()], dtype=torch.float32)
    probs = model_clf(grid)               # Shape: (N, 3)
    preds = torch.argmax(probs, dim=1).numpy()
    preds = preds.reshape(xx.shape)

plt.figure(figsize=(6, 5))
plt.contourf(xx, yy, preds, alpha=0.3, cmap=plt.cm.Set1)
plt.scatter(X_clf_np[:, 0], X_clf_np[:, 1], c=y_clf_np, edgecolor='k', cmap=plt.cm.Set1)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Multi-class Logistic Regression Decision Boundaries")
plt.show()
