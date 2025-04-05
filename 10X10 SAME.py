import random

def generate_random_numbers():
    numbers = [random.randint(1, 100) for _ in range(100)]
    for i in range(10):
        print(" ".join(f"{num:3d}" for num in numbers[i*10:(i+1)*10]))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_prime_numbers():
    for num in range(1, 101):
        if is_prime(num):
            print(f"{num:3d}", end=" ")
        else:
            print(" * ", end=" ")

def display_composite_numbers():
    for num in range(1, 101):
        if is_prime(num):
            print(" * ", end=" ")
        else:
            print(f"{num:3d}", end=" ")

def display_even_numbers():
    for num in range(1, 101):
        if num % 2 == 0:
            print(f"{num:3d}", end=" ")
        else:
            print(" * ", end=" ")

def display_odd_numbers():
    for num in range(1, 101):
        if num % 2 != 0:
            print(f"{num:3d}", end=" ")
        else:
            print(" * ", end=" ")

def main():
    while True:
        print("\na.) Generate and display 100 random numbers in 10x10 format.")
        print("b.) Display prime numbers, * everything else")
        print("c.) Display composite numbers, * else everything")
        print("d.) Display even numbers, * everything else")
        print("e.) Display odd numbers, * everything else")
        print("f.) Close program.")
        choice = input("\nEnter your choice (a, b, c, d, e, f): ")
        if choice == "a":
            generate_random_numbers()
        elif choice == "b":
            display_prime_numbers()
        elif choice == "c":
            display_composite_numbers()
        elif choice == "d":
            display_even_numbers()
        elif choice == "e":
            display_odd_numbers()
        elif choice == "f":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
