import torch
print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.cuda.get_device_name(0))

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

gpu_tensor = torch.ones(3,3, device=device)
print(gpu_tensor)

cpu_tensor = torch.rand(2,2)
gpu_tensor = cpu_tensor.to(device)
back_to_cpu = gpu_tensor.to("cpu")
print(cpu_tensor,"\n",gpu_tensor,"\n", back_to_cpu)
