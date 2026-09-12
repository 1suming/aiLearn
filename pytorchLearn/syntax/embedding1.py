# %matplotlib inline
import torch 
import matplotlib.pyplot as plt

from torch import nn 

# 5 个 token，每个 token 用 3 维向量表示

embedding=nn.Embedding(
    num_embeddings=5,
    embedding_dim=3,
)

x=torch.tensor([0,2,4])

out=embedding(x)

print("embeding weight shape:")
print(embedding.weight.shape)

print("\ninput:")
print(x)

print("\noutput:")
print(out)

print("\noutput shape:")
print(out.shape)

print(embedding(x))
print(embedding.weight[x])