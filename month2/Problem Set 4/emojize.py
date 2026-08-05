import emoji

text = input("Text: ")
result = emoji.emojize(text, language='alias')

print(f"Output: {result}")
