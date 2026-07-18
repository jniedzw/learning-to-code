def main():
    x, operator, z = input("Expression: ").split()
    x = int(x)
    z = int(z)

    match operator:
        case "+":
            result = x + z
        case "-":
            result = x - z
        case "*":
            result = x * z
        case "/":
            result = x / z
        case _:
            print("Unsupported operator")
            return

    print(f"{result:.1f}")


if __name__ == "__main__":
    main()


    
    