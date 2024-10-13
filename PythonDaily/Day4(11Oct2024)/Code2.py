# Create a class-based stack implementation with methods for push, pop, peek, and checking if the stack is empty.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self .items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek into an empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def main():
    stack = Stack()

    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Get size")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the item to push: ")
            stack.push(item)
            print("Item pushed successfully!")
        elif choice == "2":
            try:
                item = stack.pop()
                print("Popped item:", item)
            except IndexError as e:
                print(e)
        elif choice == "3":
            try:
                item = stack.peek()
                print("Top item:", item)
            except IndexError as e:
                print(e)
        elif choice == "4":
            if stack.is_empty():
                print("Stack is empty.")
            else:
                print("Stack is not empty.")
        elif choice == "5":
            print("Stack size:", stack.size())
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()