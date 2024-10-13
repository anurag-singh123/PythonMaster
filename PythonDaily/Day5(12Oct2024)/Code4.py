# Write a Python function to flatten a list of lists into a single list (without using built-in itertools.chain()).

def flatten_list(list_of_lists):
    flattened_list = []
    for sublist in list_of_lists:
        flattened_list.extend(sublist)
    return flattened_list

# Example usage
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = flatten_list(list_of_lists)
print("Flattened list:", flattened)