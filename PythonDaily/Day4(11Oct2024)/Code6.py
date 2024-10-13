# Implement a queue using two stacks in Python.

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def size(self):
        return len(self.stack1) + len(self.stack2)

# Example usage:
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Queue size:", q.size())  # prints 3
print("Dequeued item:", q.dequeue())  # prints 1
print("Queue size:", q.size())  # prints 2
print("Dequeued item:", q.dequeue())  # prints 2
print("Queue size:", q.size())  # prints 1
print("Dequeued item:", q.dequeue())  # prints 3
print("Queue size:", q.size())  # prints 0
print("Is queue empty?", q.is_empty())  # prints True