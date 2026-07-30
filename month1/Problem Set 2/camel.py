s = input("Camel Case: ")
result = ""

for c in s:
    if c.isupper():
        result += "_" + c.lower()
  
    else:
        result += c
print(result)


       
       