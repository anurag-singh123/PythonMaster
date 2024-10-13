# Write a Python program to implement a binary search algorithm that searches for a number in a sorted list.

def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def get_user_input():

    user_list = input("Enter a sorted list of numbers (separated by spaces): ")
    sorted_list = [int(num) for num in user_list.split()]

    target = int(input("Enter the target number to search for: "))

    return sorted_list, target

def main():
    sorted_list, target = get_user_input()
    result = binary_search(sorted_list, target)

    if result != -1:
        print(f"Target {target} found at index {result}.")
    else:
        print(f"Target {target} not found in the list.")

if __name__ == "__main__":
    main()