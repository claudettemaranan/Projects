lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



def char_to_number(char):
    if char in lowercase:
        number = lowercase.index(char) + 1
        return number
    elif char in uppercase:
        number = uppercase.index(char) + 1
        return number 



def main():
    while True:
        text = input("\nInput text: ")
 
        if not text.isalpha():
            print("\nInput contains invalid characters. Please enter letters only.")
            continue

        converted = []

        for char in text:
            result = char_to_number(char)
            converted.append(result)

        print("Converted: ", *converted)

        retry = input("\nDo you want to run the program again?(yes/no): ")

        if retry != "yes":
          print("\nThank you for using the converter!")
          break



main()











