import torch
X = torch.ones((3,4))
numpy_x = X.numpy()

Y = torch.from_numpy(numpy_x)

#if size 1 tensor:
a = torch.tensor([3.5])
a.item()
float(a)
int(a)