# %matplotlib inline
import torch 
import matplotlib.pyplot as plt
from torch import nn 

class LinearRegModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.weights = nn.Parameter(torch.randn(1, 
                                                dtype=torch.float),
                                                requires_grad=True)
        self.bias = nn.Parameter(torch.randn(1, 
                                             dtype=torch.float,
                                             requires_grad=True))

    #Foward defines the computation in the model
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.weights * x + self.bias
        

torch.manual_seed(42)
## Create an instance of the model (this is a subclass of nn.Module that contains nn.Parameter(s))

model_0=LinearRegModel()
# Check the nn.Parameter(s) within the nn.Module subclass we created
print(list(model_0.parameters()))

