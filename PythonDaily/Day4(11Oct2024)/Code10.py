# Write a Python function to find the intersection point (if any) of two linked lists.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    
    # Calculate the lengths of both linked lists
    lenA, lenB = 0, 0
    tempA, tempB = headA, headB
    while tempA:
        lenA += 1
        tempA = tempA.next
    while tempB:
        lenB += 1
        tempB = tempB.next

    # Move the longer list forward by the difference in lengths
    if lenA > lenB:
        for _ in range(lenA - lenB):
            headA = headA.next
    else:
        for _ in range(lenB - lenA):
            headB = headB.next

    # Move both lists forward in tandem and check for intersection
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next

    # No intersection found
    return None

# Example usage:
# Create two linked lists with an intersection point
# List A: 1 -> 2 -> 3 -> 4 -> 5
# List B: 6 -> 7 -> 4 -> 5
headA = ListNode(1)
headA.next = ListNode(2)
headA.next.next = ListNode(3)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)

headB = ListNode(6)
headB.next = ListNode(7)
headB.next.next = headA.next.next  # Intersection point

# Find the intersection point
intersection = getIntersectionNode(headA, headB)
if intersection:
    print("Intersection point:", intersection.val)  # 4
else:
    print("No intersection found.")