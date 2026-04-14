# ================= VALIDATION =================
def validate_number(num, base):
    if not num:
        return False

    if base == "A":  # Decimal
        return num.isdigit()

    elif base == "B":  # Binary
        return all(c in "01" for c in num)

    elif base == "C":  # Octal
        return all(c in "01234567" for c in num)

    elif base == "D":  # Hexadecimal
        return all(c.upper() in "0123456789ABCDEF" for c in num)

    return False


# ================= TO DECIMAL =================
def to_decimal(num, base):
    if base == "A":
        return int(num)

    elif base == "B":
        return int(num, 2)

    elif base == "C":
        return int(num, 8)

    elif base == "D":
        return int(num, 16)


# ================= FROM DECIMAL =================
def from_decimal(num, base):
    if num == 0:
        return "0"

    if base == "A":
        return str(num)

    elif base == "B":
        return bin(num)[2:]

    elif base == "C":
        return oct(num)[2:]

    elif base == "D":
        return hex(num)[2:].upper()


# ================= MAIN CONVERSION =================
def convert_number(num, from_base, to_base):
    decimal = to_decimal(num, from_base)
    return from_decimal(decimal, to_base)


# ================= MAIN PROGRAM =================
while True:
    print("\n** Numbering System Converter **")
    menu1 = input("A) Insert a new number\nB) Exit program\nPlease enter your choice (A/B): ").upper()

    if menu1 == "B":
        print("Exiting program")
        break

    elif menu1 == "A":
        number = input("Please insert a number: ").strip()

        print("** Select the base you are converting FROM **")
        menu2 = input("A) Decimal\nB) Binary\nC) Octal\nD) Hexadecimal\nChoice: ").upper()

        if menu2 not in ["A", "B", "C", "D"]:
            print("Invalid choice")
            continue

        # Validation
        if not validate_number(number, menu2):
            print("❌ Invalid number for selected base")
            continue

        print("** Select the base you are converting TO **")
        menu3 = input("A) Decimal\nB) Binary\nC) Octal\nD) Hexadecimal\nChoice: ").upper()

        if menu3 not in ["A", "B", "C", "D"]:
            print("Invalid choice")
            continue

        result = convert_number(number, menu2, menu3)
        print("Result:", result)

    else:
        print("Please select a valid choice")