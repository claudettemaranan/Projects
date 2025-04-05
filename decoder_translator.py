import os



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



def file_content(content, choice):
    if choice == 6:
        return content
    
    result = []
    
    for line in content.splitlines():
        line_result = []  
        
        for word in line.split():
            if all(c in "01" for c in word):  
                line_result.append(binary_to_code(word, choice))
                
            elif all(c in "01234567" for c in word):  
                line_result.append(octal_to_code(word, choice))
                
            elif all(c in "0123456789" for c in word):
                line_result.append(decimal_to_code(word, choice))
                
            elif all(c in "ABCDEFabcdef0123456789" for c in word):  
                line_result.append(hexadecimal_to_code(word, choice))
                
            else:  
                for char in word:
                    line_result.append(text_to_code(char, choice))
                    
        result.append(" ".join(line_result))  

    return "\n".join(result)  


def main():
    while True:
        
        file_name = input("Enter file name: ").strip()
        
        if not os.path.isfile(file_name):
            print("\nFile does not exist. Please try again.)
            continue

        with open(file_name, 'r') as file:
            content = file.read()

        while True:
            print("\nConversion Format:")
            print("1. Text")
            print("2. Decimal")
            print("3. Binary")
            print("4. Octal")
            print("5. Hexadecimal")
            print("6. No Changes")
            print("7. Exit")
        
            while True:
                try:
                    choice = int(input("\nYour choice: ").strip())
                    
                    if choice not in [1, 2, 3, 4, 5, 6, 7]:
                        print("\nInvalid input! Please enter a number between 1 and 7.")
                        continue
                    break
                except :
                    print("\nInvalid input! Please enter a number between 1 and 7.")

            if choice == 7:
                print("\nThank you for using the File Conversion Program. Goodbye!")    
                return
        
            print("\nTranslation result: ")
            result = file_content(content, choice)
            print(result)

            translate_again = input(f"\nDo you want to translate {file_name} into a different convertion format? (yes/no): ").strip().lower()

            if translate_again != "yes":
                break
            
        save_choice = input("\nDo you want to save the recently translated output in the original or new file? (original/new): ").strip().lower()

        if save_choice == "original":
            with open(file_name, "w") as save_file:
                save_file.write(result)

            print(f"\nYour file has been saved to: {file_name}")

        elif save_choice == "new":
            new_file_name = input("\nEnter new file name: ").strip()

            with open(new_file_name, "w") as save_file:
                save_file.write(result)

            print(f"\nYour file has been saved to: {new_file_name}")

        repeat = input("\nDo you want to convert another file? (yes/no): ").strip().lower()

        if repeat != "yes":
            print("Thank you for using the File Conversion Program!")
            break


main()
