def main():
    Groceries = {}

    while True:
        try:
            item = input("Item: ").strip().upper()
        except EOFError:
            break

        if item == "":
            continue

        if item in Groceries:
            Groceries[item] += 1
        else:
            Groceries[item] = 1

    for item in Groceries:
        print(f"{Groceries[item]} {item}")
            

main()
