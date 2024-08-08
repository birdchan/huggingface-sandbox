from transformers import pipeline

classifier = pipeline('ner')
x = classifier("Hello Mary, how are you? I am Brian")
print(x)
