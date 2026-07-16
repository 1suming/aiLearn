import torch 
print(torch.empty(2,3))

x=torch.tensor([2.],requires_grad=True)
y=torch.tensor([3.],requires_grad=True)

z=(x+y)*(y-2)
print("z:",z)

z.backward()
print(x.grad,y.grad)
