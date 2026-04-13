# menu 1 display
while True:
    print("Binary Calculator")
    print("A) Insert numbers")
    print("B) Exit")
    choice = input("choose a valid option: ").upper()

    if choice == 'B':
        print("Exiting program")
        break

    elif choice == 'A':

        # inserting number and making sure it`s a valid binary number
        num1 = input("insert the first number: ").strip()

        if not num1 or not set(num1).issubset('01'):
            print("Please insert a valid binary number")
            continue

        print("Please select the operation")
        print("A) Compute one's complement")
        print("B) Compute two's complement")
        print("C) Addition")
        print("D) Subtraction")
        operation = input("select an operation: ").upper()

        if operation == 'A':
            # One's complement
            result = ''.join('1' if bit == '0' else '0' for bit in num1)
            print("One's complement of", num1, "is", result)

        elif operation == 'B':
            # Two's complement (fixed)
            ones = ''.join('1' if bit == '0' else '0' for bit in num1)
            twos = bin(int(ones, 2) + 1)[2:].zfill(len(num1))
            result = twos[-len(num1):]   # keep same length
            print("Two's complement of", num1, "is", result)

        elif operation in ['C', 'D']:
            num2 = input("Please insert the second number: ").strip()

            if not num2 or not set(num2).issubset('01'):
                print("Please insert a valid binary number")
                continue

            if operation == 'C':
                # Addition
                result = bin(int(num1, 2) + int(num2, 2))[2:]
                print("The sum of", num1, "and", num2, "is", result)

            elif operation == 'D':
                # Subtraction (fixed)
                result = int(num1, 2) - int(num2, 2)

                if result < 0:
                    print("Result is negative:", result)
                else:
                    print("The difference of", num1, "and", num2, "is", bin(result)[2:])

        else:
            print("Please select a valid operation")

    else:
        print("Please select a valid choice")



#Ahmed Tarek Hassan 20230024

