import torch 
import math 

Q=torch.randn(2,4,8)
K=torch.randn(2,4,8)
V=torch.randn(2,4,8)

print("Q:",Q)

scores=Q @ K.transpose(-2,-1)
print("scores.shape:",scores.shape)


scores=scores / math.sqrt(Q.size(-1))

weights=torch.softmax(scores ,dim=-1)

output =weights @ V 

print("scores:", scores.shape)
print("weights:", weights.shape)
print("output:", output.shape)
py