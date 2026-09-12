
from collections import Counter 

words=[
    "low",
      "low",
    "low",
    "lower",
    "lowest",
]

# 1. 先把每个单词拆成字符
tokens=[list(word) for word in words]
print("初始：")
for item in tokens:
    print(item)