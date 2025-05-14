class Stack:
    # Constructor method to initialize the stack
    def __init__(self, max_size=None):
        self.items = []  # List to store stack elements
        if max_size is not None:
            self.max_size = max_size  # Optional size limit for the stack
            print(f"A stack is created with the space available for {max_size} items")
        else:
            self.max_size = None  # Unlimited stack size
            print("A stack is created.")

    # Special method to return a string representation of the stack (top to bottom)
    def __str__(self):
        return f"Stack(top -> bottom): {self.items[::-1]}"

    # Method to add an element to the top of the stack
    def push(self, item):
        if self.isFull():
            print(f"There is no room to push {item} into the stack")
        else:
            self.items.append(item)  # Add item to the end (top of the stack)
            if self.max_size != None:
                slots = self.max_size - self.size()
                print(f"{item} has been pushed successfully to the stack with {slots} slots remaining.")
            else:print(f"{item} has been pushed successfully to the stack.")
            self.display()

    # Method to remove and return the top element of the stack
    def pop(self):
        if self.isEmpty():
            print("Nothing to pop")
        else:
            popped_item = self.items.pop()  # Remove the top item
            print(f"{popped_item} has been popped from the stack.")
            if self.isEmpty():
                print("The stack is empty.")
            else:
                self.display()
                if self.max_size != None:
                    print(f"Remaining_slots: {self.max_size - self.size()}")

    # Method to return the top element without removing it
    def top(self):
        if self.isEmpty():
            print("The stack is empty")
            return None
        return self.items[-1]  # Last item in the list is the top

    # Check if the stack is empty
    def isEmpty(self):
        return len(self.items) == 0

    # Check if the stack has reached its maximum size
    def isFull(self):
        if self.max_size is None:
            return False  # Unlimited stack is never full
        return len(self.items) == self.max_size

    # Get the current number of elements in the stack
    def size(self):
        return len(self.items)

    # Print the stack visually from top to bottom
    def display(self):
        if self.isEmpty():
            print("Stack is empty.")
        else:
            size = self.size()
            print("The Stack")
            for i in range(size - 1, -1, -1):
                if i == size - 1:
                    print(f"Top -> {self.items[i]}")
                    print("----------")
                elif i == 0:
                    print(f"Bottom -> {self.items[i]}")
                else:
                    print(f"{i + 1} -> {self.items[i]}")
                    print("----------")
                
# Create a stack object and test operations
stack = Stack(10)      # Stack with a maximum of 10 items
stack.push(68)         # Push item
stack.push(54)
stack.pop()            # Pop top item
stack.push(5468)
stack.push(5896)
stack.push(54)
