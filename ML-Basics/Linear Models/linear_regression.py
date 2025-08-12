import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# Synthetic data
X = torch.rand(100,1) * 10
y = 2 * X + 3 + torch.rand(100,1) * 2

# Model
model = nn.Linear(1,1)
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
loss = 0
# Training
for epoch in range(250):
    y_pred = model(X)
    loss = loss_fn(y_pred,y)
    print(loss)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print("Trained weights: ", model.weight.item(), model.bias.item(), loss)

with torch.no_grad():
    y_pred_plot = model(X)

plt.scatter(X.numpy(), y.numpy(), label="Ground Truth")
plt.plot(X.numpy(), y_pred_plot.numpy(), color='red', label="Model Prediction")
plt.xlabel("X")
plt.ylabel('Y')
plt.legend()
plt.show()



