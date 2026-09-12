import torch
import torch.nn as nn

batch_size = 2
sequence_length = 3
embedding_dim = 4

x = torch.randn(
    batch_size,
    sequence_length,
    embedding_dim
)
print("x:",x)
linear = nn.Linear(
    embedding_dim,
    embedding_dim
)

layer_norm = nn.LayerNorm(
    embedding_dim
)

print("layer_norm:",layer_norm)
new_info = linear(x)

output = layer_norm(
    x + new_info
)

print(x.shape)
print(output.shape)
print("output:",output)