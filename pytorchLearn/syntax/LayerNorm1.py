import torch
import torch.nn as nn

#输入batch，特征维度10
x=torch.randn(4,10)

# 层归一化：对最后一个维度归一化

ln=nn.LayerNorm(normalized_shape=10)

#钱箱传播
output=ln(x)

print("输入形状:", x.shape)
print("输出形状:", output.shape)
print("n原始输入第一行:", x[0].tolist())
print("归一化后第一行:", output[0].tolist())
