# -------------------------------
# 🔗 Class: Node
# -------------------------------
# Purpose: Represents an individual element in a Linked List
# Attributes:
#   - data: (public) The value stored in the node
#   - next: (public) Reference to the next node (default is None)
# Notes:
#   - Basic building block for LinkedList
#   - Can be reused for other types of linked structures (Stack, Queue)
class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
        print(f"The node containing {self.data} is created.")

# -------------------------------
# 🔗 Class: LinkedList — Beginner-Friendly Overview
# -------------------------------
# 🚀 Purpose:
#   Implements a singly linked list using Node objects.
#   Useful when you want to store a sequence of values without using Python’s built-in list.
#   Nodes are linked together one after another in memory.
#
# 🔐 Attribute:
#   - __head (private): Points to the first node in the list.
#     If the list is empty, __head is None.
class LinkedList(Node):
# 📌 Method: __init__(self)
# -------------------------------
#   Initializes the list.
#   Sets __head = None, indicating the list starts empty.
#   Think of this like setting up an empty train with no cars yet.
    def __init__(self,__head = None):
        self.__head = __head
        self.nodes = 0
        print("A LinkedList is created.")
# 📌 Method: insert_at_end(self, data)
# -------------------------------
#   Adds a new node to the end of the linked list.
# 
#   🔢 Step-by-Step Logic:
# 
    def insert_at_end(self, data):
        
#   🧱 Step 1: Create a New Node
#       - Use the Node class to create a new node object with the given data.
#       - Set the node’s next pointer to None, since it will be added at the end.
        node = Node(data)
        self.nodes += 1
        print(f"Node{self.nodes} with the data, {data} has been added to the list.")
#   🧪 Step 2: Check if the List is Empty
#       - Look at the __head attribute to see if it is None.
#       - If __head is None, it means the list has no nodes yet.
        if self.__head == None:
#   🧠 Step 2.1: If Empty, Make New Node the Head
#       - Assign the newly created node to the __head.
#       - No further action is needed because it's the only node.
            self.__head = node
            self.display()
            
#   🔁 Step 3: Traverse to the tail of the list:
# Start from the head node and move forward using `current = current.next`
# Stop when you reach the node where `current.next` is None — that's the tail
# Then, attach the new node to `current.next`
        else:
            current = self.__head
            while current.next != None:
                current = current.next
#   🔗 Step 4: Attach the New Node
#       - Set the next pointer of the last node to point to the new node.
#       - This links the new node into the list at the end.
            current.next = node
            self.display()
            
        
#   ✅ Final Result:
#       - The new node is now added as the tail of the list.
#       - Its next remains None, and all previous nodes are unchanged.

# 📌 Method: insert_at_beginning(self, data)
# -------------------------------
#   Adds a new node to the start of the list.
#   Steps:
#     1. Create a new node with the provided data.
#     2. Set new node’s next to current head.
#     3. Update head to be the new node.
#   ✅ Efficient operation—no need to traverse the list.
    def insert_at_beginning(self, data):
        node = Node(data)
        self.__head,node.next = node,self.__head
        self.display()

# 📌 Method: delete_node(self, key)
# -------------------------------
# Deletes the first node that contains the specified key (i.e., a specific data value).
# Uses two pointers: 'current' and 'previous'.

# 🛠️ Step-by-Step Logic:
    def delete_node(self, key):
        if self.__head == None:raise ValueError("⚠️ The list is empty.")
        else:

#     1. Start with two pointers:
#        - 'current' points to the node being checked (starts at the head).
#        - 'previous' starts as None (used to track the node before 'current').
            current,previous = self.__head,None
#     2. Check if the head holds the key:
#        - If self.__head.data == key, simply move the head to the next node.
#        - This removes the current head from the list.
            if self.__head.data == key:
                print(f"The head,{self.__head.data} turned out to be the key and hence, it is removed from the list")
                self.__head = current.next
                
#     3. If the key is not at the head:
#        - Traverse the list using a loop.
#        - At each step, update 'previous' to 'current', and move 'current' to current.next.
#        - Stop when current.data == key.
            found = 0
            while current != None:
                if current.data == key:
#        - Once the key is found, update previous.next to current.next.
#        - This skips over the 'current' node, effectively deleting it.
                    previous.next = current.next
                    found = 1
                    print(f"The key,{key} has been found and hence, deleted.")
                    break                        
                else:
                    
                    previous,current = current,current.next
            if found == 0:
                raise ValueError(f"⚠️ The key,{key} is not found in the list.")
            self.display()

#
# 📌 Method: search(self, key)
# -------------------------------
#   Searches the list for a node containing the key.

#   Steps:
    def search(self, key):
#     1. Start from the head.
        current = self.__head
#     2. Traverse through each node.
        while current != None:
            if current.data == key:
                found = True
                return f"The key,{key} is found in the list."
                break
            current = current.next
        return ValueError(f"⚠️ The key,{key} is not found in the list.")
         
        

#     3. Return True if found, else False when end is reached.
#   ✅ Performs a simple linear search.
#
# 📌 Method: display(self)
# -------------------------------
#   Prints all node values in order.
#   Steps:
#     1. Start from the head.
#     2. Print each node’s data followed by an arrow (->).
#     3. End with None to show the tail.
#   ✅ Useful for visualizing list structure.
    def display(self):
        if self.__head == None:print("Empty List")
        else:
            print("-----------Linked List---------------")
            current = self.__head
            print(f"Head: {self.__head.data}")
            while current:
                print(current.data, end=" -> ")
                self.tail = current  # Update tail as we go
                current = current.next
            print("None")
            print(f"Tail: {self.tail.data}")
# -------------------------------
# 🧪 Testing Scenarios:
# -------------------------------
#   - Create an empty list and display.
#   - Add nodes at beginning and end, then display.
#   - Delete a node by value.
#   - Search for present and absent values.
#   - Display again to verify current state.

Linkedlist1 = LinkedList()
Linkedlist1.display()
Linkedlist1.insert_at_end(5)
Linkedlist1.insert_at_end(2)
Linkedlist1.insert_at_end(69)
Linkedlist1.insert_at_beginning(67)
Linkedlist1.delete_node(69)
print(Linkedlist1.search(7))