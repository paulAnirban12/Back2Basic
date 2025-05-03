# 📌 Node class represents each element (node) in the Linked List
class Node:
    def __init__(self, data):
        self.data = data        # Value/data stored in the node
        self.next = None        # Pointer to the next node
    def __repr__(self):
        return f"Node({self.data})"   # For debugging: shows Node(data)


# 📌 LinkedList class for managing the list operations
class LinkedList:
    def __init__(self):
        self.head = None        # Start of the list
        self.tail = None        # End of the list

        # Informative message about the initial state of the list
        if self.head == None and self.tail == None:
            print("An empty Linked List is created.")
        elif self.head != None and self.tail == None:
            print(f"A Linked List is created with head = {self.head}.")
        else:
            print(f"A Linked List is created with head = {self.head} and tail = {self.tail}.")

    # ✅ Check if the list is empty
    def is_empty(self):
        return self.head == None

    # ➕ Append data at the end of the list
    def append(self, data):  
        print(f"{data} is added to the list.")
        if self.is_empty():
            self.head = data    # If empty, head is set to new node
        else:
            self.tail.next = data  # Link last node to new node

        self.tail = data        # Update tail to the new node
        data.next = None        # Set new node's next as None

        # Show updated head and tail
        print(f"""The head of the list is {self.head}
The tail of the list is {self.tail}""")

    # 🔄 String representation of the entire list
    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) + " -> None"

    # ➕ Insert data at the beginning
    def prepend(self, data):
        print(f"{data} is added to the list.")

        if self.is_empty():
            self.tail = data     # If list was empty, update tail

        # New node becomes the head
        self.head, data.next = data, self.head

        print(f"""The head of the list is {self.head},
The next node is {data.next},
The tail of the list is {self.tail}""")

    # ❌ Delete a node by value
    def delete(self, data):
        if self.is_empty():
            print("The List is empty")
            return

        current, previous = self.head, None
        found = False

        while current:
            if current.data == data:
                found = True

                # Case 1: Deleting head node
                if current == self.head:
                    self.head = current.next
                    if current == self.tail:
                        self.tail = None

                # Case 2: Deleting middle or tail node
                else:
                    previous.next = current.next
                    if current == self.tail:
                        self.tail = previous
                break

            previous, current = current, current.next

        # Print outcome
        if not found:
            print(f"{data} was not found.")
        else:
            print(f"""{data} was found and deleted.
-------- Now the updated list --------
Head: {self.head}
Tail: {self.tail}""")

    # 🔍 Search for a value in the list
    def search(self, data):
        if self.is_empty():
            print("List is empty")
            return False
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    # 👁️ Display the list with head and tail
    def display(self):
        print("-----------Linked List---------------")
        current = self.head
        print(f"Head: {self.head}")
        while current:
            print(current.data, end=" -> ")
            self.tail = current  # Update tail as we go
            current = current.next
        print("None")
        print(f"Tail: {self.tail}")

    # 📏 Returns the length of the list
    def length(self):
        if self.is_empty():
            return 0
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

    # 🔁 Reverses the linked list in-place
    def reverse(self):
        prev, current = None, self.head
        old_head = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
        self.tail = old_head

        self.display()  # Show reversed list

    # ➕ Insert at a specific index
    def insert_at(self, index, data):
        if index < 0 or index > self.length():
            return False
        elif index == 0:
            self.prepend(data)
        else:
            current = self.head
            counter = 0
            while current:
                if counter == index - 1:
                    data.next = current.next
                    current.next = data
                    if data.next == None:
                        self.tail = data
                counter += 1
                current = current.next

        # Positional string formatting
        if index == 0:
            pos = "1st"
        elif index == 1:
            pos = "2nd"
        elif index == 2:
            pos = "3rd"
        else:
            pos = f"{index}th"
        print(f"{data} has been added to the list at the {pos} position")
        return True


# ✅ Test the Linked List Implementation
List = LinkedList()

# Create and append nodes
node1 = Node(5)
List.append(node1)
node2 = Node(67)
List.append(node2)

# Prepend nodes (add to beginning)
node3 = Node(7)
List.prepend(node3)
node4 = Node(69)
List.prepend(node4)

# Try deleting a node that doesn’t exist
List.delete(77)

# Search for a node
data = 67
if List.search(data):
    print(f"{data} has been found in the list")
else:
    print(f"{data} has not been found in the list")

# Print the length
print(List.length())

# Show the list
List.display()

# Reverse the list
List.reverse()

# Insert at index
node5 = Node(66)
if List.insert_at(2, node5):
    print(List)
