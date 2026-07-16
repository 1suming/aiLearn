import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(checkpoint)

sequence1_ids = [[200, 200, 200]]
sequence2_ids = [[200, 200]]

batch_ids=[
    [200, 200, 200],
    [200,200, tokenizer.pad_token_id],


]
batched_attention_marks=[
    [1,1,1],
    [1,1,0],
]
print(model(torch.tensor(sequence1_ids)).logits)
print(model(torch.tensor(sequence2_ids)).logits)

outputs=model(
    torch.tensor(batch_ids),
    attention_mask=torch.tensor( batched_attention_marks)
)
print(outputs.logits)
