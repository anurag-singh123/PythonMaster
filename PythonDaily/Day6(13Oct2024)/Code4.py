# Write a Python program with some functions and create unit tests using the unittest library to test the correctness of your functions.

# math_operations.py

import sys
import unittest

def add_numbers(numbers):
    """
    Adds a list of numbers and returns the result
    """
    result = 0
    for num in numbers:
        result += num
    return result

def multiply_numbers(a, b):
    """
    Multiplies two numbers and returns the result
    """
    return a * b

def divide_numbers(a, b):
    """
    Divides two numbers and returns the result
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

class FileManager:
    def __init__(self, file_path, mode):
        """
        Initializes the file manager with the file path and mode
        """
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        """
        Opens the file and returns the file object
        """
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Closes the file
        """
        if self.file:
            self.file.close()

def process_file(file_manager):
    """
    Processes the file by reading its contents
    """
    with file_manager as file:
        contents = file.read()
        print(f"File contents: {contents}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python math_operations.py <number1> <number2> ...")
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

    file_path = "example.txt"
    mode = "r"

    file_manager = FileManager(file_path, mode)
    process_file(file_manager)

class TestMathOperations(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers([2, 3]), 5)
        self.assertEqual(add_numbers([-2, 3]), 1)
        self.assertEqual(add_numbers([-2, -3]), -5)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(2, 3), 6)
        self.assertEqual(multiply_numbers(-2, 3), -6)
        self.assertEqual(multiply_numbers(-2, -3), 6)

    def test_divide_numbers(self):
        self.assertEqual(divide_numbers(6, 2), 3)
        self.assertEqual(divide_numbers(-6, 2), -3)
        self.assertEqual(divide_numbers(-6, -2), 3)

        with self.assertRaises(ValueError):
            divide_numbers(6, 0)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        unittest.main()
    else:
        main()