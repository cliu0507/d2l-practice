import torch
X = torch.ones((3,4))
Y = torch.zeros((3,4))

before = id(Y)
Y = Y + X
print(id(Y) == before) # result is false, meaning = will not update in memory, instead, it will repoint to a new memory

'''
important note: above behavior is not desirable in ML, because we hope to change in place

we should use:
'''
print(id(Y))
Y[:] = X + Y
Y += X

print(id(Y))
