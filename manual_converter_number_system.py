def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    
    binary = ""

    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //=2

    return binary



def decimal_to_octal(decimal): 
    if decimal == 0:
        return "0"

    octal = ""
    
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8

    return octal



def decimal_to_hexadecimal(decimal): 
    if decimal == 0:
        return "0"

    hexadecimal = ""
    hex_chars = "0123456789ABCDEF"

    while decimal > 0:
        hexadecimal = hex_chars[decimal % 16] + hexadecimal
        decimal //= 16

    return hexadecimal



def binary_to_decimal(binary):
    decimal = 0
    power = 0

    for i in binary[::-1]:
        decimal += int(i) * (2 ** power)
        power += 1

    return decimal



def binary_to_octal(binary):
        while len(binary) % 3 != 0:
                  binary = "0" + binary

        octal = ""

        for  i in range(0, len(binary), 3):
                   group = binary[i:i+3]
                   octal += str(int(group, 2))

        return octal



def binary_to_hexadecimal(binary):
        while len(binary) % 4 != 0:
                  binary = "0" + binary

        hexadecimal = ""
        
        for i in range(0, len(binary), 4):
                group = binary[i:i+4]
                hexadecimal += hex(int(group, 2))[2:].upper()

        return hexadecimal




def hexadecimal_to_decimal(hexadecimal):
    decimal = 0
    power = 0
    hex_chars = "0123456789ABCDEF"
  
    for i in hexadecimal[::-1]:
        decimal += hex_chars.index(i.upper()) * (16 ** power)
        power += 1
    
    return decimal



def hexadecimal_to_binary(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal) 
    return decimal_to_binary(decimal)



def hexadecimal_to_octal(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal) 
    return decimal_to_octal(decimal)



def octal_to_decimal (octal):
    decimal = 0
    power = 0
 
    for i in octal[::-1]:
        decimal += int(i) * (8 ** power)
        power += 1

    return decimal



def octal_to_binary (octal):
    decimal = octal_to_decimal(octal) 
    return decimal_to_binary(decimal)



def octal_to_hexadecimal (octal):
    decimal = octal_to_decimal(octal) 
    return decimal_to_hexadecimal(decimal)



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

