# we can still perform elementwise op on two tensors of different shapes
'''
mechanism

1. expand one or both arrays by copying elements so that after transformation, two tensors have the same shape
2. carry out the elementwise operations on the resulting arrays

exp:
a => shape [3,1]
b => shape [1,2]

firstly 
a will be copy to shape [3,2]
b will be copy to shape [3,2] too
then do elementwise a + b
'''
import torch
a = torch.arange(3).reshape((3,1))
b = torch.arange(2).reshape((1,2))

c = a + b
print(c)