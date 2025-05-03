# Linked List Class Implementation

# Step 1: Define the Node Class
# A Node represents a single element in the linked list.
# Node Attributes:
# - data: The value stored in the node (can be any data type).
# - next: A reference (pointer) to the next node in the list. Initially, this will be None.
# Node Methods:
# - __init__(self, data): Initializes the node with the given data and sets the next pointer to None.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"   
# Step 2: Define the LinkedList Class
# The LinkedList class manages the nodes and provides operations to manipulate the list.
# LinkedList Attributes:
# - head: A reference to the first node in the list. Initially, this will be None.
# - (optional) tail: A reference to the last node in the list. Used for efficiency in some operations.
# LinkedList Methods:
# 1. __init__(self): Initializes the linked list with the head (and optionally tail) set to None.
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        if self.head == None and self.tail == None:
            print("An empty Linked List is created.")
        elif self.head != None and self.tail == None:
            print(f"A Linked List is created with head = {self.head}.")
        else:
            print(f"A Linked List is created with head = {self.head} and tail = {self.tail}.")
# 2. is_empty(self): 
# - Returns True if the list is empty (head is None), otherwise returns False.
    def is_empty(self):
        if self.head == None:return True
        return False
# 3. append(self, data): 
# - Adds a new node with the given data at the end of the list.
# - If the list is empty, the new node becomes the head.
# - Otherwise, traverse to the last node and update its next pointer.
# node1 = Node(5)
# node2 = Node(78,node1)
# List = LinkedList()
# List.append(node1)
# List.append(node2)
# List  5
    def append(self, data):  # append(data = node2 = Node(78, 5))
    # Step 1: Check if the list is empty.
        print(f"{data} is added to the list.")
        if self.is_empty():
            self.head = data  # If the list is empty, set the head to the first node (node1 with value 5).
        else:
            self.tail.next = data
            # # Step 2: If the list is not empty, traverse the list to find the last node.
            # current = self.head  # Start from the head of the list (current = node1 with value 5).
            # while current.next:  # Keep traversing as long as there's a next node.
            #     print(f"Traversing node: {current.data}")  # Print current node data as you traverse.
            #     current = current.next  # Move to the next node (current = node2).

            # # Step 3: Once the last node is reached, set its next pointer to the new node (node2).
            # current.next = data  # current.next (which is node1.next) now points to node2.

        # Step 4: Update the tail to the newly added node.
        self.tail = data  # The tail is now node2 (with value 78).
        data.next = None
        # Print the head and tail to confirm the list structure.
        print(f"""The head of the list is {self.head}
The tail of the list is {self.tail}""")

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) + " -> None"

# 4. prepend(self, data):
# Purpose:
# - Adds a new node at the **beginning** of the linked list.
    
# Step-by-Step Explanation:

# Step 1: Check the current head of the list.
# - The list might already have nodes.
# - The current head will become the second node after this operation.
    def prepend(self, data):
        print(f"{data} is added to the list.")
# Step 2: Link the new node to the existing list.
# - Set the `next` pointer of the new node (`data.next`) to the current head.
# - This connects the new node to the rest of the list.
        if self.is_empty():self.tail = data
# Step 3: Update the head of the list.
# - Assign the new node (`data`) as the new head of the list.
# - This makes the new node the first element.
        self.head,data.next = data,self.head
# Step 4: Optional tail update.
# - If the list was empty before, also set the tail to this new node.
        
        print(f"""The head of the list is {self.head},
The next node is {data.next},
The tail of the list is {self.tail}""")
# Final Result:
# - The new node is now at the beginning.
# - The previous head is now the second node.
# - All other nodes follow in order.

# Example:
# Before: Head → A → B → None
# After : Head → X → A → B → None

# 5. delete(self, data): 
# Purpose:
# - Removes the first node in the linked list that contains the specified value (`data`).
    def delete(self, data):
    

        # Step 1: Check if the list is empty.
        # - If head is None, the list is empty. Nothing to delete.
        if self.is_empty():
            print("The List is empty")
            return

        # Step 2: Check if head contains the target value.
        # - If so, update head to head.next.
        # - If head is also the tail, set tail to None.

        # Step 3: Traverse to find the node to delete (if not in head).
       
        current, previous = self.head, None
        found = False
            # - Move through the list until match is found or end is reached.
        while current:
            if current.data == data:
                found = True

                # - If deleting the tail, update the tail pointer.
                if current == self.head:
                    self.head = current.next
                    if current == self.tail:
                        self.tail = None
                else:
                # - Unlink the node by skipping it.
                    previous.next = current.next
                    if current == self.tail:
                        self.tail = previous
                break

            # - Advance both pointers.
            previous, current = current, current.next

        # Step 4: Final result message.
        # - If not found, inform the user.
        # - If deleted, show updated head and tail.
        if not found:
            print(f"{data} was not found.")
        else:
            print(f"""{data} was found and deleted.
-------- Now the updated list --------
Head: {self.head}
Tail: {self.tail}""")

# Result:
# - The list remains intact except for the first node that matched the target value, which is removed.


# 6. search(self, data)
# Purpose:
# - Checks whether a node with the specified `data` exists in the linked list.
# - Returns True if found, otherwise returns False.

# Step-by-Step Logic:
# 1. If the list is empty (i.e., self.head is None), return False immediately.
    def search(self, data):
        found = False
        if self.is_empty():print("List is empty")
        else:
# 2. Start from the head node and begin traversing the list.
            current = self.head
# 3. At each node, compare the node’s data with the target `data`.
            while current:
            
                if current.data == data:
                    node = current
                    return True
                else:
                    current = current.next
            return False
            
# 4. If a match is found, return True.
# 5. If no match is found and the end of the list is reached (current becomes None), return False.
            
# Example:
# - List: 10 → 20 → 30 → None
# - search(20) → True
# - search(40) → False

# Note:
# - This is a linear search with time complexity O(n).


# 7. display(self): 
# - Prints or returns a list of the data values from all nodes, starting from the head.
    def display(self):
        print("-----------Linked List---------------")
        current = self.head
        print(f"Head:{self.head}")
        while current:
            print(current.data, end=" -> ")
            self.tail = current
            current = current.next
        print("None")
        print(f"Tail:{self.tail}")
# 8. length(self): 
# - Returns the number of nodes in the list by traversing from the head to the end.
    def length(self):
        if self.is_empty():return 0
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length
        # return len(self)
# 9. reverse(self):
# - This method reverses the order of nodes in the linked list.
# - It flips the direction of all the next pointers so that the last node becomes the head and the head becomes the tail.

# Step-by-step explanation:

# 1. Initialize three pointers:
#    - prev: Initially set to None; this will eventually become the new tail.
#    - current: Starts at the head of the list; used to traverse through the list.
#    - next_node: Temporarily holds the next node so we don’t lose access to the rest of the list during reassignment.
    def reverse(self):
        prev,current = None,self.head
        old_head = self.head
# 2. Traverse the list:
#    - While current is not None:
#      - Store the next node (current.next) in next_node.
#      - Reverse the link by setting current.next to prev.
#      - Move prev to current.
#      - Move current to next_node.
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        self.tail = old_head
# 3. After the loop ends:
#    - prev is now the new head of the list.
#    - Assign head = prev to complete the reversal.
#    - (Optional) If maintaining a tail pointer, update tail to the old head.
        self.display()
# Example:
# Before reverse:
# Head → 1 → 2 → 3 → None
#
# After reverse:
# Head → 3 → 2 → 1 → None
#
# The list is now reversed in place.

# 10. insert_at(self, index, data):
# - This method inserts a new node with the specified `data` at the given `index` in the linked list.
# - It rearranges pointers to insert the node without breaking the existing structure.

# Step-by-step explanation:

# 1. Handle invalid indexes:
#    - If index < 0, the position is invalid.
#    - If index > length of the list, it's out of range (unless appending at the end is allowed).
#    - If index == 0, delegate to `prepend()` since it's just inserting at the start.
    def insert_at(self, index, data):
        if index < 0 or index > self.length():return False
        elif index == 0:self.prepend(data)
        else:
# 2. Traverse to the node before the target index:
#    - Start from the head of the list.
#    - Use a counter to keep track of how many steps you've moved.
#    - Stop when you reach the node just before the desired position (index - 1).
#    - Keep a reference to this node — this is the node after which you will insert the new one.
            current = self.head
            counter = 0
            while current:
                
                if counter == index-1:
# 3. Link the new node in:
#    - Set the `next` pointer of the new node to point to the current node's `next` (the node that was originally at the target index).
#    - Update the current node’s `next` to point to the new node.
#    - This effectively "inserts" the node into the chain at the correct position.
                    data.next = current.next
                    current.next = data
# 4. Update tail if inserted at the end:
#    - If the new node’s `next` is `None`, it indicates that it's now the last node.
#    - Since the new node is the last one, update the `tail` reference of the list to point to this new node.
#    - This ensures that the tail always points to the last node in the list, maintaining the correct structure.
                    if data.next == None:self.tail = data
                
                counter += 1
                current = current.next
        if index == 0:pos = "1st"
        elif index == 1:pos = "2nd"
        elif index == 2:pos = "3rd"
        else:pos = f"{index}th"
        print(f"{data} has been added to the list at the {pos} position")
        return True
# Example:
# - Original List: A → B → C → None
# - Operation: insert_at(index=1, data=X)
# - Result: A → X → B → C → None


# Step 3: Test the LinkedList Implementation
# - Test appending and prepending nodes to the list.
# - Test searching for a node in the list.
# - Test deleting a node from the list.
# - Test displaying the list and calculating the length.
# - Optionally, test reversing the list.

List = LinkedList()
node1 = Node(5)
List.append(node1)
node2 = Node(67)
List.append(node2)
node3 = Node(7)
List.prepend(node3)
node4 = Node(69)
List.prepend(node4)
List.delete(77)
data = 67
if List.search(data):print(f"{data} has been found in the list")
else:print(f"{data} has not been found in the list")
print(List.length())
List.display()
List.reverse()
node5 = Node(66)
if List.insert_at(2,node5):print(List)

