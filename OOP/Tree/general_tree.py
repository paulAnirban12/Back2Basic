# =============================================================================
# 🌳 General Tree (N-ary) Using OOP - With Explanatory Comments
# =============================================================================

class TreeNode:
    def __init__(self, data):
        self.data = data                  # Holds the data of the node
        self.children = []               # List to store child nodes
    
    def is_leaf(self):
        if self.children == []:
            return "Leaf Node"           # If no children, it's a leaf node
        return self.children             # Otherwise, return the list of children


class GeneralTree:
    def __init__(self):
        self.__root = None               # Root of the tree (private)
        self.nodes = []                  # List of all nodes in the tree
        self.pre_order = []              # Stores nodes during pre-order traversal
        self.post_order = []             # Stores nodes during post-order traversal


    def add_root(self, data):
        # Adds the root node if not already set
        if self.is_empty():
            root = TreeNode(data)
            self.__root = root
            print(f"The node, {data} is the root node of the tree.")
            self.nodes.append(self.__root)
        else:
            print(f"The tree already has {self.__root.data} as root")


    def add_child(self, parent_node, datas):
        # Adds multiple children to a parent node if it's in the tree
        if parent_node in self.nodes:
            for data in datas:
                node = TreeNode(data)
                parent_node.children.append(node)
                self.nodes.append(node)
                print(f"As the node,{parent_node.data} is a part of the tree, so its child, {node.data} also become a part of the tree.")
        else:
            print(f"⚠️ The parent node, {parent_node.data} not a part of the tree.")


    def search(self, target):
        # Searches for a node by its data using recursion
        for node in self.nodes:
            found = self._search_recursive(node, target)
            if found is not None:
                return True
        return False


    def _search_recursive(self, current_node, target):
        # Recursive helper function to find a node
        if current_node is None:
            return None
        if current_node.data == target:
            return current_node
        for child in current_node.children:
            found = self._search_recursive(child, target)
            if found is not None:
                return found
        return None


    def traverse_pre_order(self):
        # Pre-order traversal: Root -> Left -> Right
        if self.is_empty():
            return "Tree is empty"

        for node in self.nodes:
            def _visit(node):
                if node not in self.pre_order:
                    self.pre_order.append(node)
                for child in node.children:
                    _visit(child)
            _visit(node)

        visual = " ->".join(f" {item.data}" for item in self.pre_order)
        return f"""---------Preorder Output------------
{visual}"""


    def traverse_post_order(self):
        # Post-order traversal: Left -> Right -> Root
        if self.is_empty():
            return "Tree is empty."

        def _post_order_recursive(node):
            for child in node.children:
                _post_order_recursive(child)
            self.post_order.append(node)

        _post_order_recursive(self.__root)

        visual = " -> ".join(f"{node.data}" for node in self.post_order)
        return f"""------------PostOrder Traversal------------------------
{visual}"""


    def is_empty(self):
        # Checks if tree is empty (no root)
        return self.__root is None


    def get_root(self):
        # Returns the root node
        if self.is_empty():
            return None
        return self.__root


    def size(self):
        # Returns the total number of nodes in the tree using recursion
        return self._size_recursive(self.__root)


    def _size_recursive(self, node):
        # Recursive helper for size calculation
        size = 1
        for child in node.children:
            size += self._size_recursive(child)
        return size


    def remove_node(self, target):
        # Removes a node and its entire subtree from the tree

        if self.is_empty():
            return "Tree is empty."

        if self.__root.data == target:
            # Remove the entire tree if root is the target
            self.__root = None
            self.nodes.clear()
            return f"Root node '{target}' and entire tree removed."

        def find_parent(current_node):
            # Helper to find parent of target node
            for child in current_node.children:
                if child.data == target:
                    return current_node
                result = find_parent(child)
                if result:
                    return result
            return None

        parent_node = find_parent(self.__root)

        if parent_node:
            for child in parent_node.children:
                if child.data == target:
                    def remove_subtree(node):
                        # Recursive function to remove all descendants
                        for sub in node.children:
                            remove_subtree(sub)
                        if node in self.nodes:
                            self.nodes.remove(node)

                    parent_node.children.remove(child)
                    remove_subtree(child)
                    return f"Node '{target}' and its subtree removed."

            return f"Node '{target}' not found under located parent."
        else:
            return f"Node '{target}' not found in the tree."


    def height(self):
        # Returns the height of the tree
        if self.is_empty():
            return -1
        return self._height_recursive(self.__root)


    def _height_recursive(self, node):
        # Recursive helper to calculate tree height
        if not node.children:
            return 0
        child_heights = [self._height_recursive(child) for child in node.children]
        return 1 + max(child_heights)


    def clear(self):
        # Clears the entire tree
        if self.is_empty():
            return "Tree is already empty."
        else:
            self.__root = None
            self.nodes.clear()
            self.pre_order.clear()
            self.post_order.clear()
            print("The tree has been successfully cleared")
            return self.nodes


    def update_node_data(self, target, new_data):
        # Updates the data of a node if found

        if self.is_empty():
            return "Tree is empty."

        self.pre_order.clear()
        self.traverse_pre_order()
        print("Traversal (Pre Order) Before Update:")
        visual_before = " -> ".join(f"{node.data}" for node in self.pre_order)
        print(visual_before)

        found = self._search_recursive(self.get_root(), target)
        if found:
            prev = found.data
            found.data = new_data
            print(f"Node data updated successfully from {prev} to {found.data}.")

            self.pre_order.clear()
            self.traverse_pre_order()
            print("Traversal (Pre Order) After Update:")
            visual_after = " -> ".join(f"{node.data}" for node in self.pre_order)
            return visual_after

        return "Target data not found in the tree."


    def print_tree(self, node=None, level=0):
        # Prints the tree structure visually (like a file directory)

        if self.is_empty():
            print("Tree is empty.")
            return

        if node is None:
            node = self.__root

        if level == 0:
            print(f"{str(node.data)} ──> Root")
        else:
            print("    " * (level - 1) + "└── " + str(node.data))

        for child in node.children:
            self.print_tree(child, level + 1)


# ===================== TESTING SECTION ==========================

tree = GeneralTree()

# Add root node
tree.add_root(5)
root = tree.get_root()

# Add children to root
tree.add_child(root, [69, 87, 56])

# Check if a node is a leaf
node1 = root.children[1]
print(node1.is_leaf())

# Add children to an internal node
tree.add_child(node1, [698, 857, 156])

# Search for a value
if tree.search(875):
    print("Found")
else:
    print("Not Found")

# Print tree traversal
print(tree.traverse_pre_order())
print(tree.traverse_post_order())

# Size calculations
print(tree.size())
print(tree._size_recursive(node1))

# Remove a node and its subtree
print(tree.remove_node(857))

# Height of the tree
print(tree.height())

# Update node data
print(tree.update_node_data(698, 69))

# Visual representation of the tree
tree.print_tree()

# Clear the entire tree
print(tree.clear())

# Traversals after clearing
print(tree.traverse_pre_order())
print(tree.traverse_post_order())
