# Lambda Functions with Map and Filter
# Use lambda functions with map() and filter() to:
    # Square every number in a list using map().
    # Filter out even numbers from a list using filter().

numbers = [1, 2, 3, 4, 5, 6, 7, 8,  9, 10]

# Square every number in a list using map()
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)

# Filter out even numbers from a list using filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Filter out odd numbers from a list using filter()
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd numbers:", odd_numbers)