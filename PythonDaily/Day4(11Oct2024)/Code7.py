# Write a Python program to find the Kth largest element in an unsorted array.

import heapq

def find_kth_largest(nums, k):

    # Create a min-heap and push all elements from the array into the heap
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)

    # Pop elements from the heap k-1 times
    for _ in range(k-1):
        heapq.heappop(min_heap)

    # The top element of the heap is the Kth largest element
    return min_heap[0]

# Example usage:
nums = [3, 2, 1, 5, 6, 4]
k = 2
result = find_kth_largest(nums, k)
print(f"The {k}th largest element is {result}")