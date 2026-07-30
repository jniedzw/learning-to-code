def main():
    total = 0
    while total < 50:
        coin = int(input("Insert Coin: "))
        if coin in (25, 10, 5):
            total += coin
        if total < 50:
            print(f"Amount Due: {50 - total}")
    print(f"Change Owed: {total - 50}")

if __name__ == "__main__":
    main()
