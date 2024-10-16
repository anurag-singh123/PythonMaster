# Write a Python program that takes a list of numbers and calculates the sum of even numbers and the sum of odd numbers separately using loops and conditionals.

def calculate_sums(numbers):
    even_sum = 0
    odd_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return even_sum, odd_sum

numbers = [1, 2, 3, 4, 5, 6]
even_sum, odd_sum = calculate_sums(numbers)

print("Even sum:", even_sum)
print("Odd sum:", odd_sum)

