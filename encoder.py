def main():
    while True:

        while True:
            try:
                num_lines = int(input("\nHow many lines do you plan to encode?: "))
            except:
                print("\nPlease enter a valid numerical value!")
                continue
            

            print(f"\nEnter {num_lines} of input")

            lines = []

            for i in range(1, num_lines + 1):
                user_input = input(f"Line {i}: ")
                lines.append(user_input)

            add_more = input("\nDo you want to add more input? (yes/no): ").lower()

            if add_more != "yes":
                break
            
        while True:
            file_name = input("\nEnter the filename to save the encoded lines: ")

            if not file_name.endswith(".txt"):
                file_name += ".txt"

            with open(file_name, "w") as file:
                file.write("\n".join(lines))

            print(f"\nEncoded lines have been saved to {file_name}.")
            break

        repeat = input("\nDo you want to create another file? (yes/no): ").lower()

        if repeat != "yes":
            print("\nThank you for using the File Conversion Program!")
            break


main()
