s = input("Input: ")
result = ""
for c in s:
    if c.lower() in ("a", "e", "i", "o", "u"):
        pass
    else:
        result += c
print(result)   