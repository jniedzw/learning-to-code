def main():
    percentage = get_fuel_percentage()
    if percentage <= 1:
        print("E")

    elif percentage >= 99:
        print("F")

    else:
        print(f"{percentage}%")

def get_fuel_percentage():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            
            if y == 0:
                continue
            
            if x > y:
                continue

            percentage = round((x / y) * 100)
            return percentage

        except ValueError:
            continue
    
        except ZeroDivisionError:
            continue

main()


