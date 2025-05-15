# Node class represents each element in the stack
class Node:
    def __init__(self, data, next=None):
        self.data = data          # Value stored in the node
        self.next = next          # Pointer to the next node

# Stack class uses linked list logic (LIFO)
class Stack:
    def __init__(self, __top=None):
        self.__top = __top        # Private pointer to top node of the stack
        if self.is_empty():       # Check if stack is empty on creation
            print("⚠️  An empty Stack")
        else:
            size = self.size() + 1
            print(f"A stack is created with top value,{self.__top} and the size is {size}")

    def push(self, data):
        node = Node(data)             # Create new node with data
        node.next = self.__top        # Link new node to current top
        self.__top = node             # Update top to new node
        self.display()                # Show current state of stack

    def pop(self):
        if self.__top == None:
            raise ValueError("⚠️  Stack underflow as empty stack.")  # Cannot pop from empty stack
        else:
            node = self.__top             # Save current top
            self.__top = node.next        # Move top pointer down
            print(f"The previous head,{node.data} has been popped.")
            self.display()                # Show updated stack

    def peek(self):
        if self.__top == None:
            raise ValueError("⚠️  Stack underflow as empty stack.")  # Cannot peek on empty stack
        else:
            print(f"Output:{self.__top.data}")   # Show top value

    def is_empty(self):
        return self.__top == None    # Returns True if stack is empty

    def size(self):
        size = 0
        current = self.__top
        while current:               # Traverse through nodes
            size += 1
            current = current.next
        return size                  # Return number of nodes

    def display(self):
        if self.is_empty():
            pass                     # Do nothing if empty
        else:
            print("-----------Stack---------------")
            print(f"Top: {self.__top.data}")
            current = self.__top
            while current:
                print(f"""{current.data}
↓""")                               # Show each element
                bottom = current
                current = current.next
            print("None")
            print(f"Bottom: {bottom.data}")
            print(f"Total Nodes:{self.size()}")

# Test the stack
stack1 = Stack()
stack1.push(5)       # Push 5 onto the stack
stack1.push(69)      # Push 69 on top of 5
stack1.push(420)     # Push 420 on top of 69
stack1.pop()         # Pop 420 from the top
stack1.peek()        # Peek should return 69
