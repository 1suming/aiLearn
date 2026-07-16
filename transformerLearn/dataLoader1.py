from torch.utils.data import Dataset 
import json 
import torch
from torch.utils.data import DataLoader
from transformers import AutoTokenizer

checkpoint="bert-base-chinese"
tokenizer=AutoTokenizer.from_pretrained(checkpoint)


class AFQMC(Dataset):
    def __init__(self,data_file):
        self.data= self.load_data(data_file)
    
    def load_data(self,data_file):
        Data={}
        with open(data_file,"rt",encoding="utf-8") as f:
            for idx,line in enumerate(f):
                sample=json.loads(line.strip())
                Data[idx]=sample 
        return Data 
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self,idx):
        return  self.data[idx]
    
train_data=AFQMC("D:/00AI/datasets/afqmc_public/train.json")
valid_data = AFQMC('D:/00AI/datasets/afqmc_public/dev.json')
print(train_data[0])

def collate_fn(batch_samples):
    batch_setence_1,batch_setence_2 =[],[]
    batch_label=[]

    for sample in batch_samples:
        batch_setence_1.append(sample["sentence1"])
        batch_setence_2.append(sample["sentence2"])
        batch_label.append(int(sample["label"]))

    x =tokenizer(
        batch_setence_1,
        batch_setence_2,
        padding=True, 
        truncation=True,
        return_tensors="pt"
    )
    y=torch.tensor(batch_label)
    return x,y

train_dataloader=DataLoader(train_data,batch_size=4,shuffle=True,collate_fn=collate_fn)

batch_X,batch_y= next(iter(train_dataloader))
print('batch_X shape:', {k: v.shape for k, v in batch_X.items()})
print('batch_y shape:', batch_y.shape)
print(batch_X)
print(batch_y)