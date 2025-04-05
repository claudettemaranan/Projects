import random

def generate_random_numbers():
    return [random.randint(1, 100) for _ in range(100)]

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_prime_numbers(random_numbers):
    modified_table = []
    for num in random_numbers:
        if is_prime(num):
            modified_table.append(f"{num:3d}")
        else:
            modified_table.append(" * ")
    display_table(random_numbers, modified_table)

def display_composite_numbers(random_numbers):
    modified_table = []
    for num in random_numbers:
        if is_prime(num):
            modified_table.append(" * ")
        else:
            modified_table.append(f"{num:3d}")
    display_table(random_numbers, modified_table)

def display_even_numbers(random_numbers):
    modified_table = []
    for num in random_numbers:
        if num % 2 == 0:
            modified_table.append(f"{num:3d}")
        else:
            modified_table.append(" * ")
    display_table(random_numbers, modified_table)

def display_odd_numbers(random_numbers):
    modified_table = []
    for num in random_numbers:
        if num % 2 != 0:
            modified_table.append(f"{num:3d}")
        else:
            modified_table.append(" * ")
    display_table(random_numbers, modified_table)

def display_table(original_numbers, modified_table):
    original_table = [original_numbers[i * 10:(i + 1) * 10] for i in range(10)]
    for i in range(10):
        print(" ".join(f"{original_table[i][j]:3d}" if modified_table[i * 10 + j] != " * " else " * " for j in range(10)))

def main():
    while True:
        print("\na.) Generate and display 100 random numbers in 10x10 format.")
        print("b.) Display prime numbers, * everything else")
        print("c.) Display composite numbers, * everything else")
        print("d.) Display even numbers, * everything else")
        print("e.) Display odd numbers, * everything else")
        print("f.) Close program.")
        choice = input("\nEnter your choice (a, b, c, d, e, f): ")
        if choice == "a":
            print("\nOriginal:")
            random_numbers = generate_random_numbers()
            display_table(random_numbers, random_numbers)
        elif choice == "b":
            print("\nOriginal:")
            random_numbers = generate_random_numbers()
            display_table(random_numbers, random_numbers)
            print("\nNew:")
            display_prime_numbers(random_numbers)
        elif choice == "c":
            print("\nOriginal:")
            random_numbers = generate_random_numbers()
            display_table(random_numbers, random_numbers)
            print("\nNew:")
            display_composite_numbers(random_numbers)
        elif choice == "d":
            print("\nOriginal:")
            random_numbers = generate_random_numbers()
            display_table(random_numbers, random_numbers)
            print("\nNew:")
            display_even_numbers(random_numbers)
        elif choice == "e":
            print("\nOriginal:")
            random_numbers = generate_random_numbers()
            display_table(random_numbers, random_numbers)
            print("\nNew:")
            display_odd_numbers(random_numbers)
        elif choice == "f":
            break
        else:
            print("\nInvalid choice!")

if __name__ == "__main__":
    main()


