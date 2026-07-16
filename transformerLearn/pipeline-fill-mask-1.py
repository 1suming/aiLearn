from transformers import pipeline

unmasker=pipeline("fill-mask")
results=unmasker("this course will teach you all about <mask> models.",top_k=2)
print(results)
