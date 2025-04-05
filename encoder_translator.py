def text_to_code(word, choice):
    if choice == 1:
        return word
    elif choice == 2:
        decimal = str(ord(word))
        return decimal
    elif choice == 3:
        binary = bin(ord(word))[2:]
        return binary
    elif choice == 4:
        octal = oct(ord(word))[2:]
        return octal
    elif choice == 5:
        hexadecimal = hex(ord(word))[2:]
        return hexadecimal



def decimal_to_code(word, choice):
    if choice == 1:
        text = chr(word)
        return text
    elif choice == 2:
        decimal = str(word)
        return decimal
    elif choice == 3:
        binary = bin(word)[2:]
        return binary
    elif choice == 4:
        octal = oct(word)[2:]
        return octal
    elif choice == 5:
        hexadecimal = hex(word)[2:].upper()
        return hexadecimal



def binary_to_code(word, choice):
    if choice == 1:
        text = chr(int(word, 2))
        return text
    elif choice == 2:
        decimal = str(int(word, 2))
        return decimal
    elif choice == 3:
        return word
    elif choice == 4:
        octal = oct(int(word, 2))[2:]
        return octal
    elif choice == 5:
        hexadecimal = hex(int(word, 2))[2:].upper()
        return hexadecimal



def octal_to_code(word, choice):
    if choice == 1:
        text = chr(int(word, 8))
        return text
    elif choice == 2:
        decimal = str(int(word, 8))
        return decimal
    elif choice == 3:
        binary = bin(int(word, 8))[2:]
        return binary
    elif choice == 4:
        return word
    elif choice == 5:
        hexadecimal = hex(int(word, 8))[2:].upper()
        return hexadecimal



def hexadecimal_to_code(word, choice):
    if choice == 1:
        text = chr(int(word, 16))
        return text
    elif choice == 2:
        decimal = str(int(word, 16))
        return decimal
    elif choice == 3:
        binary = bin(int(word, 16))[2:]
        return binary
    elif choice == 4:
        octal = oct(int(word, 16))[2:]
        return octal
    elif choice == 5:
        return word



def encoded_lines(lines, choice):
    if choice == 6:
        return lines
        
    result = []

    for line in lines:
        line_result = []

        for word in line.split():
            if all(c == "0" or c == "1" for c in word):
                line_result.append(binary_to_code(word, choice))

            elif all(c in "01234567" for c in word):  
                line_result.append(octal_to_code(word, choice))

            elif all(c in "0123456789" for c in word):
                line_result.append(decimal_to_code(int(word), choice))

            elif all(c in "ABCDEFabcdef0123456789" for c in word):  
                line_result.append(hexadecimal_to_code(word, choice))

            else:  
                for char in word:
                    line_result.append(text_to_code(char, choice))

        result.append(" ".join(line_result))

    return result



def main():
    all_encoded_lines = []

    while True:
        try:
            num_lines = int(input("\nHow many lines will you encode?: "))
        except:
            print("\nPlease enter a valid numerical value!")
            continue

        print(f"\nEnter the {num_lines} lines of input:")

        lines = []

        for i in range(1, num_lines + 1):
            user_input = input(f"Line {i}: ")
            lines.append(user_input)

        print("\nOutput Type:")
        print("1. Text")
        print("2. Decimal")
        print("3. Binary")
        print("4. Octal")
        print("5. Hexadecimal")
        print("6. No Changes")
        print("7. Exit")

        while True:
            try:
                choice = int(input("\nChoice: "))
                
                if choice not in [1, 2, 3, 4, 5, 6, 7]:
                    print("Please enter a number between 1 and 7.")
                    continue
                break
            except:
                print("\nPlease enter a number.")

        if choice == 7: 
            print("\nThank you for using the File Conversion Program. Goodbye!")
            break

        encoded_lines_result = encoded_lines(lines, choice)
        all_encoded_lines.extend(encoded_lines_result)

        print("\nEncoded Lines: ")
        for encoded in all_encoded_lines:
            print(encoded)

        add_more = input("\nDo you want to add more input? (yes/no): ").lower()

        if add_more != "yes":
            break

    while True:
        file_name = input("\nEnter the filename to save the encoded lines: ")

        if not file_name.endswith('.txt'):
            file_name += '.txt'

        try:
            with open(file_name, 'w', encoding='utf-8') as file:
                for encoded in all_encoded_lines:
                    file.write(encoded + '\n')
                
            print(f"\nEncoded lines have been saved to '{file_name}'.")
            break
        except Exception as e:
            print(f"An error occurred while saving to the file: {e}")

    repeat = input("\nDo you want to create another file? (yes/no): ").lower()

    if repeat != "yes":
        print("Thank you for using the File Conversion Program!")


main()
