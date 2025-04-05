import random
import statistics



def highest_number(numbers):
    highest = numbers[0]

    for num in numbers:
        if num > highest:
            highest = num
            
    return highest
 


def lowest_number(numbers):
    lowest = numbers[0]

    for num in numbers:
        if num < lowest:
            lowest = num
            
    return lowest



def ascending_order(numbers):
    return sorted(numbers)



def descending_order(numbers):
    return sorted(numbers, reverse = True)



def main():
    while True:
        option = input("\nDo you want to enter numbers manually or generate random numbers? (enter/generate): ")

        if option.strip().lower() == "enter": 
            while True:
                try:
                    quantity = int(input("\nEnter the quantity of positive numbers: "))

                    if quantity > 0:
                        break
                except:
                    print("\nInvalid input. Please enter a positive number.")

            numbers = []

            for i in range(quantity):
                while True:
                    try:
                        if i + 1 == 1:
                            suffix = "st"
                        elif i + 1 == 2:
                            suffix = "nd"
                        elif i + 1 == 2:
                            suffix = "rd"
                        else:
                            suffix = "th"
                            
                        num = int(input(f"\nEnter the {i+1}{suffix}  number: "))
                        numbers.append(num)
                        break
                    except:
                        print("\nInvalid input. Please enter a number.")


        elif option.strip().lower() == "generate":
            while True:
                try:             
                    quantity = int(input("\nEnter the total quantity of numbers to be generated: "))

                    if quantity > 0:
                        break
                    else:
                        print("\nPlease enter a positive number.")                               
                except:
                    print("\nPlease enter a positive number.")                               
              
            while True:
                try:
                    min_num = int(input("\nEnter the minimum number: "))
                    break
                except:
                    print("\nPlease enter a number")
          
            while True:
                try:
                    max_num = int(input("Enter the maximum number: "))
                    
                    if max_num > min_num:
                        break
                    else:
                        print("\nInvalid input. The maximum number must be greater than the minimum number.\n")
                except:
                    print("\nPlease enter a number")

            numbers = []
            
            for i in range(quantity):
                generate_numbers = random.randint(min_num, max_num)
                numbers.append(generate_numbers)


        else: 
            print("\nInvalid choice. Please enter 'enter' or 'generate'.")
            continue


        print("\nNumbers entered: ", numbers)
        print("Highest number:", highest_number(numbers))
        print("Lowest number:", lowest_number(numbers))
        print("Ascending order:", ascending_order(numbers))
        print("Descending order:", descending_order(numbers))
        print("Average: ", sum(numbers) / len(numbers))
        print("Median: ", statistics.median(numbers))

        retry = input("\nDo you want to run the program again? (yes/no): ")

        if retry.strip().lower() != "yes":
            print("\nThank you for using the Number Sorter!")
            break

main()
