# Binary Tree Implementation in Python with detailed comments
# File: Back2Basic/OOP/Tree/binary_tree.py

# -------------------------------
# Node class - represents a single node in the tree
# -------------------------------
class Node:
    # Each node holds data and pointers to left and right child nodes
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # Useful for debugging – shows the value inside the node
    def __repr__(self):
        return f"Node({self.data})"


# -------------------------------
# BinaryTree class - manages the whole tree
# -------------------------------
class BinaryTree:
    # Constructor initializes the root of the tree
    def __init__(self, root=None):
        self.root = root

    # Nicely formats the tree when printed (visual hierarchy)
    def __repr__(self):
        lines = []
        self._display_tree(self.root, lines, "", "", is_root=True)
        return "\n".join(lines)

    # Helper method to recursively print the tree structure
    def _display_tree(self, node, lines, prefix, child_label, is_root=False):
        if node is not None:
            # Show root node
            if is_root:
                lines.append(f"{node.data} ──> Root")
            else:
                lines.append(f"{prefix}{child_label}── {node.data}")

            # Adjust spacing for child nodes
            child_prefix = prefix + ("│   " if child_label == "├" else "    ")

            # Add children with visual markers
            children = []
            if node.left:
                children.append(("├", "(L)", node.left))
            if node.right:
                children.append(("└", "(R)", node.right))

            # Recurse for each child
            for connector, label, child in children:
                self._display_tree(child, lines, child_prefix, connector + label)

    # Insert a new node into the tree (BST logic)
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            print(f"{data} has become the root of the tree")
            return

        # Internal recursive insertion method
        def _insert(current):
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    print(f"As {data} < {current.data}, inserted to left")
                else:
                    _insert(current.left)
            else:
                if current.right is None:
                    current.right = new_node
                    print(f"As {data} > {current.data}, inserted to right")
                else:
                    _insert(current.right)

        _insert(self.root)

    # Search for a value in the tree (DFS)
    def search(self, target):
        def _search(node):
            if node is None:
                return False
            if node.data == target:
                return True
            # Recurse into both left and right
            return _search(node.left) or _search(node.right)

        return _search(self.root)

    # Inorder Traversal: Left -> Root -> Right
    def inorder_traversal(self, node):
        if node is None:
            return []

        result = []
        result += self.inorder_traversal(node.left)
        result.append(str(node.data))
        result += self.inorder_traversal(node.right)
        return result

    # Preorder Traversal: Root -> Left -> Right
    def preorder_traversal(self, node):
        if node is None:
            return []

        result = [str(node.data)]
        result += self.preorder_traversal(node.left)
        result += self.preorder_traversal(node.right)
        return result

    # Postorder Traversal: Left -> Right -> Root
    def postorder_traversal(self, node):
        if node is None:
            return []

        result = []
        result += self.postorder_traversal(node.left)
        result += self.postorder_traversal(node.right)
        result.append(str(node.data))
        return result

    # Finds the minimum node (used in deletion)
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Recursive deletion logic
    def _delete_recursive(self, node, data):
        if node is None:
            return node

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Node found. Handle cases based on number of children
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node has two children: replace with inorder successor
            temp = self._min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete_recursive(node.right, temp.data)

        return node

    # Public delete method
    def delete(self, data):
        self.root = self._delete_recursive(self.root, data)
        print(f"{data} has been deleted from the tree (if it existed)")


# -------------------------------
# Example Usage
# -------------------------------
print("\n--- Simple Example Usage ---")

# Step 1: Create a tree
my_tree = BinaryTree()

# Step 2: Insert values
my_tree.insert(10)
my_tree.insert(5)
my_tree.insert(15)
my_tree.insert(2)
my_tree.insert(7)
my_tree.insert(13)
my_tree.insert(69)

# Step 3: Visualize structure
print(my_tree)

# Step 4: Traversals
print("Inorder Traversal:")
print(" -> ".join(my_tree.inorder_traversal(my_tree.root)))

print("Preorder Traversal:")
print(" -> ".join(my_tree.preorder_traversal(my_tree.root)))

print("Postorder Traversal:")
print(" -> ".join(my_tree.postorder_traversal(my_tree.root)))

# Step 5: Search
print("Search for 7:", my_tree.search(7))   # Should be True
print("Search for 99:", my_tree.search(99)) # Should be False

# Step 6: Delete a value
print("Delete 5:")
my_tree.delete(5)

# Step 7: Tree after deletion
print(my_tree)

print("Inorder After Deletion:")
print(" -> ".join(my_tree.inorder_traversal(my_tree.root)))
