import os
import re



def text(word, choice):
    if choice == 1:
        return word



def decimal_to_text(word, choice):
    if choice == 1:
        text = chr(word)
        return text



def binary_to_text(word, choice):
    if choice == 1:
        text = chr(int(word, 2))
        return text



def octal_to_text(word, choice):
    if choice == 1:
        text = chr(int(word, 8))
        return text



def hexadecimal_to_text(word, choice):
    if choice == 1:
        text = chr(int(word, 16))
        return text



def replace_consonants(content, char):
    return re.sub(r'[^aeiou\s]', char, content, flags=re.IGNORECASE)



def replace_vowels(content, char):
    return re.sub(r'[aeiou]', char, content, flags=re.IGNORECASE)



def replace_char(content, letters, char):
    return re.sub(f'[{letters}]', char, content, flags=re.IGNORECASE)



def replace_word(content, word, replacement):
    return content.replace(word, replacement)



def file_content(content, choice):
    result = []
    
    for line in content.splitlines():
        line_result = []
        
        for word in line.split():
            if all(c in "01" for c in word):
                line_result.append(binary_to_text(word, choice))
                
            elif all(c in "01234567" for c in word):
                line_result.append(octal_to_text(word, choice))
                
            elif all(c in "0123456789" for c in word):
                line_result.append(decimal_to_text(int(word), choice))
                
            elif all(c in "ABCDEFabcdef0123456789" for c in word):
                line_result.append(hexadecimal_to_text(word, choice))
                
            else:
                for char in word:
                    line_result.append(text(char, choice))
                    
        result.append(" ".join(line_result))
        
    return "\n".join(result)



def main():
    while True:
        file_name = input("Enter the file name: ")

        if not os.path.isfile(file_name):
            print("\nFile does not exist.\n")
            continue

        with open(file_name, "r") as file:
            content = file.read()

        print("\nContent:")
        print(content)

        while True:
            print("\nChoose an option:")
            print("1. Convert to text")
            print("2. Replace consonants with chosen character/s")
            print("3. Replace vowels with chosen character/s")
            print("4. Choose character/s to replace")
            print("5. Choose word to replace")
            print("6. Exit")

            try:
                choice = int(input("\nChoice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == 1:
                converted_text = file_content(content, choice)
                
            elif choice == 2:
                char = input("Chosen Character: ").strip()
                converted_text = replace_consonants(content, char)
                
            elif choice == 3:
                char = input("Chosen Character: ").strip()
                converted_text = replace_vowels(content, char)
                
            elif choice == 4:
                letters = input("Character/s to replace (e.g., @ 2 c): ").strip()
                char = input("Chosen Character: ").strip()
                converted_text = replace_char(content, letters, char)

            elif choice == 5:
                word = input("Word to replace: ").strip()
                replacement = input("Replace with: ").strip()

                converted_text = replace_word(content, letters, char)

            elif choice == 6:
                break

            else:
                print("Invalid choice, please try again.")
                continue

            print("\nOutput:")
            print(converted_text)

            further_changes = input("\nAny further changes?(yes/no): ").strip().lower()
            if further_changes != "yes":
                break

        save_choice = input("\nDo you want to save the output in the original or new file?(original/new): ").strip().lower()

        if save_choice == "original":
            with open(file_name, "w") as save_file:
                save_file.write(converted_text)
                
            print(f"\nYour file has been saved to: {file_name}")
            
        elif save_choice == "new":
            new_file_name = input("\nEnter new file name: ")
            
            with open(new_file_name, "w") as save_file:
                save_file.write(converted_text)
                
            print(f"\nYour file has been saved to: {new_file_name}")

        repeat = input("\nDo you want to work with another file?(yes/no): ").strip().lower()

        if repeat != "yes":
            print("Thank you for using the File Conversion Program!")
            break


main()
