from transformers import pipeline

# generator=pipeline("text-generation")
generator=pipeline("text-generation",model="distilgpt2")

results=generator("in this course ,we will teach you how to")
print(results)

# results =generator(
#     "In this course, we will teach you how to",
#     num_return_sequences=2,
#     max_length=50,
# )
# print(results)