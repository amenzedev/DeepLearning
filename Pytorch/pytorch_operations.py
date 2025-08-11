import torch
a = torch.rand(2,2)
b = torch.rand(2,2)

print("Tensor A: ", a)
print("Tensor B: ", b)

c = a + b
print(c)

d = a * b
print(d)

e = torch.matmul(a,b)
print(e)