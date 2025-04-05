import os

def main():
    while True:

        while True:
            file_name = input("\nEnter file name: ")

            if not os.path.isfile(file_name):
                print("\nFile does not exist. Please try again.")
                continue
            
            with open(file_name, "r") as file:
                 content = file.read()
                 
            print("\nContent: ")
            print(content)
            break

        repeat = input("\nDo you want to decode another file?(yes/no): ").strip().lower()

        if repeat != "yes":
            print("\nThank you for using the File Decoder Program!")
            break

main()


