import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression, make_classification
import numpy as np

# =========================================================
# 1️⃣ MULTIVARIABLE LINEAR REGRESSION
# =========================================================

# --- Create synthetic regression dataset ---
X_reg_np, y_reg_np = make_regression(
    n_samples=200, n_features=2, noise=10, coef=False, random_state=42
)
X_reg = torch.tensor(X_reg_np, dtype=torch.float32)
y_reg = torch.tensor(y_reg_np, dtype=torch.float32).view(-1, 1)

# --- Define linear regression model ---
model_reg = nn.Linear(2, 1)  # 2 input features → 1 output

# --- Loss & optimizer ---
loss_fn_reg = nn.MSELoss()
optimizer_reg = torch.optim.SGD(model_reg.parameters(), lr=0.01)

# --- Training loop ---
for epoch in range(500):
    y_pred_reg = model_reg(X_reg)
    loss = loss_fn_reg(y_pred_reg, y_reg)

    optimizer_reg.zero_grad()
    loss.backward()
    optimizer_reg.step()

print("Linear Regression Weights:", model_reg.weight.data.numpy())
print("Linear Regression Bias:", model_reg.bias.data.numpy())

# --- Plot regression results ---
with torch.no_grad():
    y_pred_plot = model_reg(X_reg).numpy()

plt.figure(figsize=(6, 5))
plt.scatter(range(len(y_reg_np)), y_reg_np, label="Ground Truth", alpha=0.6)
plt.scatter(range(len(y_pred_plot)), y_pred_plot, color="red", label="Prediction", alpha=0.6)
plt.xlabel("Sample Index")
plt.ylabel("Target Value")
plt.title("Multivariable Linear Regression: Predictions vs Truth")
plt.legend()
plt.show()