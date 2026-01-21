class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Add an element to the stack"""
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        """Remove and return the top element"""
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        return self.stack.pop()

    def peek(self):
        """Return the top element without removing it"""
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.stack[-1]

    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.stack) == 0

    def size(self):
        """Return the number of elements in the stack"""
        return len(self.stack)

    def display(self):
        """Display stack elements"""
        print("Stack:", self.stack)
