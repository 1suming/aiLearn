from torch import nn
from transformers import AutoModel
import torch 


device="cuda" if torch.cuda.is_available() else "cpu"

class BertForPairwiseCLS(nn.Module):
    