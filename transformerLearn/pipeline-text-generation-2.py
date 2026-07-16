from transformers import pipeline

# generator=pipeline("text-generation")
generator=pipeline("text-generation",model="uer/gpt2-chinese-poem")

results =generator(
       "[CLS] 万 叠 春 山 积 雨 晴 ，",
    num_return_sequences=2,
    max_length=40,
)
print(results)