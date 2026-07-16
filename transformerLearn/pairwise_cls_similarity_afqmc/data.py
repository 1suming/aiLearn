import json
from torch.utils.data import Dataset, DataLoader
import torch 

class AFQMC(Dataset):
    def __init__(self, data_file):
        self.data = self.load_data(data_file)
    
    def load_data(self, data_file):
        Data = {}
        with open(data_file, 'rt') as f:
            for idx, line in enumerate(f):
                sample = json.loads(line.strip())
                Data[idx] = sample
        return Data
    
    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

train_data=AFQMC("D:/00AI/datasets/afqmc_public/train.json")
valid_data = AFQMC('D:/00AI/datasets/afqmc_public/dev.json')

print(train_data[0])


def get_dataLoander(args,dataset,tokenizer,batch_size=None,shuffle=None):
    def collote_fn(batch_samples):
        batch_sentence_1, batch_sentence_2 = [], []
        batch_label = []
        for sample in batch_samples:
            batch_sentence_1.append(sample['sentence1'])
            batch_sentence_2.append(sample['sentence2'])
            batch_label.append(int(sample['label']))
        X = tokenizer(
            batch_sentence_1, 
            batch_sentence_2, 
            max_length=args.max_seq_length,
            padding=True, 
            truncation=True, 
           return_tensors="pt"
        )
        y=torch.tensor(batch_label)
        return X,y 
    
    return DataLoader(
        dataset,
        batch_size=(batch_size if batch_size else args.batch_size), 
        shuffle=shuffle, 
        collate_fn=collote_fn
    )

train_dataloader = DataLoader(train_data, batch_size=4, shuffle=True, collate_fn=collote_fn)
