# Write a Python function that takes a list and a target sum, and returns all unique pairs of numbers in the list that add up to the target sum.

def find_pairs(nums, target_sum):
    
    num_set = set()
    pairs = set()

    for num in nums:
        complement = target_sum - num
        if complement in num_set:
            # We've found a pair, add it to the set of pairs
            pair = tuple(sorted((num, complement)))
            pairs.add(pair)
        num_set.add(num)

    return list(pairs)

# Example usage:
nums = [1, 2, 3, 4, 5, 6]
target_sum = 7
result = find_pairs(nums, target_sum)
print("Pairs that add up to", target_sum, ":")
for pair in result:
    print(pair)