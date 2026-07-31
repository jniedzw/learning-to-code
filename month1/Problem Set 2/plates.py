def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s.isalnum():
        return False
    if len(s) < 2 or len(s) > 6:  
        return False
    if not s[0:2].isalpha(): 
        return False    

    seen_digit = False       

    for c in s:
        if c.isalpha() and seen_digit:
            return False
        elif c.isdigit():
            if not seen_digit and c == "0":
                return False
            seen_digit = True

    return True          

main()


