#convert from decimal to binary
def decimal_to_binary(decimal_number):
  binary = ""
  while int(decimal_number) > 0:
    remainder = int(decimal_number) % 2
    binary = str(remainder) + binary
    decimal_number = int(decimal_number) // 2
  return (binary)
"""Example:
result = decimal_to_binary(55)
print(result)
"""

#convert from decimal to octal

def decimal_to_octal(decimal_number):
   octal = ""
   while int(decimal_number) > 0:
      remainder = int(decimal_number) % 8
      octal = str(remainder) + octal
      decimal_number = int(decimal_number) // 8
   return octal
"""Example:
result = decimal_to_octal(55)
print(result)
"""

#convert from decimal to hexadecimal
def decimal_to_hexadecimal(decimal_number):
   hexadecimal_digits = "0123456789ABCDEF"
   hexadecimal = ""
   while int(decimal_number) > 0:
      remainder = int(decimal_number) % 16
      hexadecimal= hexadecimal_digits[remainder] + hexadecimal
      decimal_number = int(decimal_number) // 16
   return hexadecimal
"""Example:
result = decimal_to_hexadecimal(205)
print(result)
"""

#convert from binary to decimal
def binary_to_decimal(binary_num):
    decimal = 0
    power = 0           #The power of base
    while int(binary_num) > 0:
        digit = int(binary_num) % 10
        decimal = decimal + digit * (2 ** power)
        binary_num = int(binary_num) // 10
        power += 1
    return decimal
"""Example:
result = binary_to_decimal(1011)
print(result)
"""

#convert from octal to decimal
def octal_to_decimal(octal_num):
    decimal = 0
    power = 0        #The power of base
    while int(octal_num) > 0:
        digit = int(octal_num) % 10
        decimal = decimal + digit * (8 ** power)
        octal_num = int(octal_num) // 10
        power += 1
    return decimal
"""Example:
result = octal_to_decimal(2360)
print(result)
"""

#convert from hexadecimal to decimal
def hexadecimal_to_decimal(hexadecimal_num):
    hexadecimal_digits = "0123456789ABCDEF"
    hexadecimal_num = hexadecimal_num.upper()
    decimal = 0

    for digit in hexadecimal_num:
        if digit in hexadecimal_digits:
            decimal = decimal * 16 + hexadecimal_digits.index(digit)

    return decimal
"""Example:
result = hexadecimal_to_decimal("12E")
print(result)
"""

#convert from binary to octal
def binary_to_octal(binary_num):
    octal = ""
    decimal = 0
    power = 0        #The power of base
    #convert from binary to decimal
    while int(binary_num) > 0:
        digit = int(binary_num) % 10
        decimal += digit * (2 ** power)
        binary_num = int(binary_num) // 10
        power += 1
        #convert from decimal to octal
    while decimal > 0:
        remainder = decimal % 8
        octal = str(remainder) + octal
        decimal = decimal // 8
    return int(octal)
"""Example:
result = binary_to_octal(10101)
print(result)
"""

#convert from binary to hexadecimal
def binary_to_hexadecimal(binary_num):
    hexadecimal_digits = "0123456789ABCDEF"
    hexadecimal = ""
    decimal = 0
    power = 0         #The power of base
    #convert from binary to decimal
    while int(binary_num) > 0:
        digit = int(binary_num) % 10
        decimal += digit * (2 ** power)
        binary_num = int(binary_num) // 10
        power += 1
        #convert from decimal to hexadecimal
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hexadecimal_digits[remainder] + hexadecimal
        decimal = decimal // 16
    return hexadecimal
"""Example:
result = binary_to_hexadecimal(11011)
print (result)
"""

#convert from octal to binary
def octal_to_binary(octal_num):
    binary = ""
    decimal = 0
    power = 0       #The power of base
    # Convert from octal to decimal
    while int(octal_num) > 0:
        digit = int(octal_num) % 10
        decimal = decimal + digit * (8 ** power)
        octal_num = int(octal_num) // 10
        power += 1
    # Convert from decimal to binary
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    return int(binary)
"""Example:
result = octal_to_binary(52)
print(result)
"""

#convert from octal to hexadecimal
def octal_to_hexadecimal(octal_num):
    hexadecimal_digits = "0123456789ABCDEF"
    hexadecimal = ""
    decimal = 0
    power = 0       #The power of base
    # Convert from octal to decimal
    while int(octal_num) > 0:
        digit = int(octal_num) % 10
        decimal = decimal + digit * (8 ** power)
        octal_num = int(octal_num) // 10
        power += 1
    # Convert from decimal to hexadecimal
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hexadecimal_digits[remainder] + hexadecimal
        decimal = decimal // 16
    return hexadecimal
"""Example:
result = octal_to_hexadecimal(52)
print(result)
"""

#convert from hexadecimal to binary
def hexadecimal_to_binary(hexadecimal_num):
    binary = ""
    decimal = 0
    hexadecimal_digits = "0123456789ABCDEF"
    # Convert from hexadecimal to decimal
    hexadecimal_num = hexadecimal_num.upper()
    for digit in hexadecimal_num:
        if digit in hexadecimal_digits:
            decimal = decimal * 16 + hexadecimal_digits.index(digit)
    # Convert from  decimal to binary
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    return int(binary)
"""Example:
result = hexadecimal_to_binary("4F")
print(result)
"""


#Main program
def select_function(num,menu2,menu3):
    if menu2 == menu3:
        return num
    elif menu2 == "A" and menu3 == "B":
        return decimal_to_binary(num)
    elif menu2 == "A" and menu3 == "C":
        return decimal_to_octal(num)
    elif menu2 == "A" and menu3 == "D":
        return decimal_to_hexadecimal(num)

    elif menu2 == "B" and menu3 == "A":
        return binary_to_decimal(num)
    elif menu2 == "B" and menu3 == "C":
        return binary_to_octal(num)
    elif menu2 == "B" and menu3 == "D":
        return binary_to_hexadecimal(num)

    elif menu2 == "C" and menu3 == "A":
        return octal_to_decimal(num)
    elif menu2 == "C" and menu3 == "B":
        return octal_to_binary(num)
    elif menu2 == "C" and menu3 == "D":
        return octal_to_hexadecimal(num)

    elif menu2 == "D" and menu3 == "A":
        return hexadecimal_to_decimal(num)
    elif menu2 == "D" and menu3 == "B":
        return hexadecimal_to_binary(num)

while True:
    print("** Numbering System Converter **")
    menu1 = input("A) Insert a new number\nB) Exit program\nPlease enter your choice (A/B) : ")
    if menu1.upper() == "A":
        number_str = input("Pleas insert a number: ")
        try:
            number = str(number_str)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        while True:
            print("** Please select the base you want to convert a number from **")
            menu2 = input("A) Decimal\nB) Binary\nC) Octal\nD) Hexadecimal\nPlease enter your choise (A/B/C/D): ")
            if menu2.upper() in ["A", "B", "C", "D"]:
                while True:
                    print("** Please select the base you want to convert a number to ** ")
                    menu3 = input(("A) Decimal\nB) Binary\nC) Octal\nD) Hexadecimal\nPlease enter your choise (A/B/C/D): "))
                    if menu3.upper() in ["A", "B", "C", "D"]:
                        menu2 = menu2.upper()
                        menu3 = menu3.upper()
                        result = select_function(number, menu2, menu3)
                        print("Result:",result)
                        break
                    else:
                        print("Please select a valid choise")
                break   #Exit the loop and go back to menu 1
            else:
                print("Please select a valid choise")
    elif menu1.upper() == "B":
        print("Exiting program")
        break            #To exit from the program
    else:
        print("Please select a valid choise")











