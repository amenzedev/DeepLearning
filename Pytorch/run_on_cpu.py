import torch

device = torch.device("cpu")

t = torch.ones(2,2, device=device)
print(t)

#check if cuda(gpu) is available
print(torch.cuda.is_available())