import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

# Data 
X_np, y_np = make_classification(n_samples=200, n_features=2, n_classes=2, n_informative=2, n_redundant=0)

X = torch.tensor(X_np, dtype=torch.float32)
y = torch.tensor(y_np, dtype=torch.float32).view(-1,1)

# model
model = nn.Sequential(
    nn.Linear(2,1),
    nn.Sigmoid()
)

#loss fn and optimizer
loss_fn = nn.BCELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

# Training
for epoch in range(200):
    y_pred = model(X)
    loss = loss_fn(y_pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

weights = model[0].weight.detach().numpy()
bias = model[0].bias.detach().numpy()
print(" (Weight,Bias) : ", weights, bias)

# 6️⃣ Plot decision boundary
with torch.no_grad():
    # Create a mesh grid over feature space
    x_min, x_max = X_np[:, 0].min() - 1, X_np[:, 0].max() + 1
    y_min, y_max = X_np[:, 1].min() - 1, X_np[:, 1].max() + 1
    xx, yy = torch.meshgrid(
        torch.linspace(x_min, x_max, 100),
        torch.linspace(y_min, y_max, 100),
        indexing='ij'
    )

    grid = torch.cat((xx.reshape(-1, 1), yy.reshape(-1, 1)), dim=1)
    probs = model(grid).reshape(xx.shape)

plt.contourf(xx, yy, probs.numpy(), levels=[0, 0.5, 1], alpha=0.3, cmap='RdBu')
plt.scatter(X_np[:, 0], X_np[:, 1], c=y_np, edgecolor='k', cmap='bwr')
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Logistic Regression Decision Boundary")
plt.show()