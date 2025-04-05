def text_to_decimal(text):
    decimal = []
 
    for char in text:
        if char.isdigit():
            decimal.append(char)  
        else:
            convert = str(ord(char)) 
            decimal.append(convert)
    
    return ' '.join(decimal)


def text_to_binary(text):
    binary = []

    for char in text:
        if char.isdigit():
            convert = bin(int(char))[2:]  
            binary.append(convert)
        else:
            convert = bin(ord(char))[2:] 
            binary.append(convert)
    
    return ' '.join(binary)


def text_to_octal(text):
    octal = []

    for char in text:
        if char.isdigit():
            convert = oct(int(char))[2:]  
            octal.append(convert)
        else:
            convert = oct(ord(char))[2:]  
            octal.append(convert)

    return ' '.join(octal)


def text_to_hexadecimal(text):
    hexadecimal = []

    for char in text:
        if char.isdigit():
            convert = hex(int(char))[2:]  
            hexadecimal.append(convert)
        else:
            convert = hex(ord(char))[2:]  
            hexadecimal.append(convert)

    return ' '.join(hexadecimal)


def main():
    while True:
        print("\nChoose a conversion format for your text:")
        print("1. Decimal")
        print("2. Binary")
        print("3. Octal")
        print("4. Hexadecimal")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice not in ["1", "2", "3", "4", "5"]:
            print("\nInvalid input! Please enter a number between 1 and 4.")
            continue  

        try:
            if choice == "1":
                text = input("\nEnter the text to convert: ")
                decimal = text_to_decimal(text)
                print("\nDecimal: ", decimal)
            elif choice == "2":
                text = input("\nEnter the text to convert: ")
                binary = text_to_binary(text) 
                print("\nBinary: ", binary)
            elif choice == "3":
                text = input("\nEnter the text to convert: ")
                octal = text_to_octal(text)
                print("\nOctal: ", octal)
            elif choice == "4":
                text = input("\nEnter the text to convert: ")
                hexadecimal = text_to_hexadecimal(text)
                print("\nHexadecimal:", hexadecimal)
            elif choice == "5":
                print("\nExiting...")
                break
        except:
            print("\nInvalid input!")

        repeat = input("\nDo you want to convert another text? (yes/no): ")

        if repeat.lower() != "yes":
            print("Thank you for using the Text Conversion Program. Goodbye!")
            break


main()
