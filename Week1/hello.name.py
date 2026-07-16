# Ask for the users name
name = input("What is your name? ").strip().title()

#split user's name into first and last name
first, last = name.split(" ")

# Greet the user by name
print(f"Hello, {first}")