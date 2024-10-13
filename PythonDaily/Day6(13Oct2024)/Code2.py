# Write a Python program that takes command-line arguments, processes them, and performs a specific operation (e.g., adding numbers passed as arguments).

import sys

def add_numbers(numbers):
    """
    Adds a list of numbers and returns the result
    """
    result = 0
    for num in numbers:
        result += num
    return result

def main():
    if len(sys.argv) < 2:
        print("Usage: python add_numbers.py <number1> <number2> ...")
        sys.exit(1)

    numbers = []
    for arg in sys.argv[1:]:
        try:
            num = float(arg)
            numbers.append(num)
        except ValueError:
            print(f"Invalid number: {arg}")
            sys.exit(1)

    result = add_numbers(numbers)
    print(f"The sum of the numbers is: {result}")

if __name__ == "__main__":
    main()