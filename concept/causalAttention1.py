import torch 
import math 

T=4

scores=torch.randn(T,T)

mask=torch.triu(
    torch.ones(T,T),
    diagonal=1,
).bool()

print("mask:",mask)
scores=scores.masked_fill(mask,float("-inf"))
print("scores:",scores)
weights = torch.softmax(scores, dim=-1)

print(weights)