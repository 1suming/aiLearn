from transformers import pipeline

classifier=pipeline("zero-shot-classification")
result=classifier(
    "this is a course about the transformers library", 
    candidate_labels=["education","politics","business"]
)
print(result)
