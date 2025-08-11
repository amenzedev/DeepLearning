import torch
import time
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

a = torch.rand(20000,20000, device=device)
b = torch.rand(20000,20000, device=device)

start = time.time()
c = torch.matmul(a,b)
gpu_time = time.time() - start
print(f"GPU time: {gpu_time:.4f} seconds")

a = a.to("cpu")
b = b.to("cpu")
start = time.time()
c = torch.matmul(a,b)
cpu_time = time.time() - start
print(f"GPU time: {cpu_time:.4f} seconds")

