def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]

    return binary



def decimal_to_octal(decimal):
    octal = oct(decimal)

    return octal



def decimal_to_hexadecimal(decimal):
    hexadecimal = hex(decimal)[2:].upper()
    
    return hexadecimal



def binary_to_decimal(binary):
    decimal = int(binary, 2)

    return decimal



def binary_to_octal(binary):
    decimal = int(binary, 2)
    octal = oct(decimal)[2:]

    return octal



def binary_to_hexadecimal(binary):
    decimal = int(binary, 2)
    hexadecimal = hex(decimal)[2:].upper()

    return hexadecimal




def hexadecimal_to_decimal(hexadecimal):
    decimal = int(hexadecimal, 16)
   
    return decimal



def hexadecimal_to_binary(hexadecimal):
    decimal = int(hexadecimal, 16)
    binary = bin(decimal)[2:]
    
    return binary



def hexadecimal_to_octal(hexadecimal):
    decimal = int(hexadecimal, 16)
    octal = oct(decimal)[2:]
    
    return octal



def octal_to_decimal (octal):
    decimal = int(octal, 8)
    
    return decimal



def octal_to_binary (octal):
    decimal = int(octal, 8)
    binary = bin(decimal)[2:]
    
    return binary



def octal_to_hexadecimal (octal):
    decimal = int(octal, 8)
    hexadecimal = hex(decimal)[2:].upper()
    
    return hexadecimal



def main():
    while True:
        print("\nConversion Menu: ")
        print("1. Decimal to Binary")
        print("2. Decimal to Octal")
        print("3. Decimal to Hexadecimal")
        print("4. Binary to Decimal")
        print("5. Binary to Octal")
        print("6. Binary to Hexadecimal")
        print("7. Hexadecimal to Decimal")
        print("8. Hexadecimal to Binary")
        print("9. Hexadecimal to Octal")
        print("10. Octal to Decimal")
        print("11. Octal to Binary")
        print("12. Octal to Hexadecimal")
        print("13. Exit")

        while True:
            try:
                choice = int(input("\nEnter your choice (1-13): "))

                if choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
                    print("\nInvalid input! Please enter a number between 1 and 13.")
                    continue
                
                break

            except:
                print("\nInvalid input! Please enter a valid number.")        

        try:
            if choice == 1:
                decimal = int(input("\nEnter a decimal number: "))
                print("Binary:", decimal_to_binary(decimal))
            elif choice == 2:
                decimal = int(input("\nEnter a decimal number: "))
                print("Octal:", decimal_to_octal(decimal))
            elif choice == 3:
                decimal = int(input("\nEnter a decimal number: "))
                print("Hexadecimal:", decimal_to_hexadecimal(decimal))
            elif choice == 4:
                binary = input("\nEnter a binary number: ")
                print("Decimal:", binary_to_decimal(binary))
            elif choice == 5:
                binary = input("\nEnter a binary number: ")
                print("Octal:", binary_to_octal(binary))
            elif choice == 6:
                binary = input("\nEnter a binary number: ")
                print("Hexadecimal:", binary_to_hexadecimal(binary))
            elif choice == 7:
                hexadecimal = input("\nEnter a hexadecimal number: ").upper()
                print("Decimal:", hexadecimal_to_decimal(hexadecimal))
            elif choice == 8:
                hexadecimal = input("\nEnter a hexadecimal number: ").upper()
                print("Binary:", hexadecimal_to_binary(hexadecimal))
            elif choice == 9:
                hexadecimal = input("\nEnter a hexadecimal number: ").upper()
                print("Octal:", hexadecimal_to_octal(hexadecimal))
            elif choice == 10:
                octal = input("\nEnter an octal number: ")
                print("Decimal:", octal_to_decimal(octal))
            elif choice == 11:
                octal = input("\nEnter an octal number: ")
                print("Binary:", octal_to_binary(octal))
            elif choice == 12:
                octal = input("\nEnter an octal number: ")
                print("Hexadecimal:", octal_to_hexadecimal(octal))
            elif choice == 13:
                print("\nExiting...")
                break
        except:
            print("\nInvalid input. Please enter a valid number.")

        retry = input("\nDo you want to run the program again?(yes/no): ")

        if retry.strip().lower() != "yes":
            print("\nThank you for using the converter!")
            break


main()





