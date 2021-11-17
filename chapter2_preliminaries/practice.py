import torch

x = torch.arange(12)
print(x.shape)
x2 = torch.arange(12, dtype=torch.float32)

x = x.reshape(3,4)
x = torch.zeros((2,3,4))

_shape = x.shape
print(_shape)

# specifiy exact values
y = torch.tensor([[1,2,3,4],[3,4,6,8]])



# concat
t1 = torch.randn(3,4) # standard gaussian distribution with mean 0 and std 1
t2 = torch.zeros(3,4)
y = torch.cat((t1, t2), dim = 0)


exit()