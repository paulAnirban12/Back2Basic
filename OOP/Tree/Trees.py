class TreeNode:
    def __init__(self, value):
        # Initialize the node with a value and an empty list of children
        self.value = value
        self.children = []
        
    def add_child(self, child_node):
        # Ensure child is a TreeNode instance, then add it to the children list
        if not isinstance(child_node, TreeNode):
            child_node = TreeNode(child_node)
        self.children.append(child_node)

    def __str__(self):
        # This helps print the node directly using its value
        return self.value

    def remove_child(self, child_node):
        # Remove the child node from the current node’s children list
        for child in self.children:
            if isinstance(child, TreeNode) and child.value == child_node:
                self.children.remove(child)
                return
        # If the child was not found
        print(f"{child_node} was never a child of {self.value}")

    def is_leaf(self):
        # Returns True if the node has no children
        return len(self.children) == 0

    def get_children(self):
        # Returns the list of child nodes
        return self.children


class Tree:
    def __init__(self, root_node):
        # Initialize the tree with a root node
        self.root_node = root_node
        self.nodes_postorder = []
        self.tree_height = 0
    
    def traverse_preorder(self, node):
        # Perform preorder traversal (visit node → children)
        node_preorder = []

        def _traverse(n):
            node_preorder.append(n)
            for child in n.children:
                _traverse(child)

        _traverse(node)
        # Format the traversal result as a string
        visual = " ->".join(f" {item.value}" for item in node_preorder)
        return f"""---------Preorder Output------------
{visual}"""
    
    def traverse_postorder(self, node):
        # Perform postorder traversal (visit children → node)
        self.nodes_postorder = []

        def _traverse(n):
            if n is None:
                print("Node is None and not part of this tree.")
                return
            for child in n.children:
                _traverse(child)
            self.nodes_postorder.append(n)

        _traverse(node)
        visual = " ->".join(f" {item.value}" for item in self.nodes_postorder)
        return f"""---------Postorder Output------------
{visual}"""

    def find(self, target_node):
        # Search the tree for the exact target_node object (not just value)
        node = self.root_node

        def _find(node, target_node):
            if node == target_node:
                return node
            for child in node.children:
                result = _find(child, target_node)
                if result:
                    return result
            return None

        result = _find(node, target_node)
        if result is None:
            return f"None to indicate the node '{target_node}' doesn't exist in this tree."
        else:
            return f"{result} — the search is successful."

    def height(self, node):
        # Calculate the height of the tree from this node (longest path to a leaf)
        max_height = 0
        if len(node.children) == 0:
            return 0  # Leaf node has height 0
        else:
            for child in node.children:
                node_height = self.height(child)  # Recursively find height
                if max_height < node_height:
                    max_height = node_height
        return max_height + 1  # Add 1 for the current level

    def count_nodes(self, node):
        # Recursively count all nodes in the subtree from this node
        total_node = 1  # Count this node
        for child in node.children:
            total_node += self.count_nodes(child)
        return total_node

    def print_tree_2d(self):
        # Print the tree visually using 2D style connectors
        def traverse(node, prefix="", is_last=True):
            connector = "└── " if is_last else "├── "
            print(prefix + connector + node.value)
            new_prefix = prefix + ("    " if is_last else "│   ")
            child_count = len(node.children)
            for i, child in enumerate(node.children):
                is_child_last = (i == child_count - 1)
                traverse(child, new_prefix, is_child_last)

        print("└── " + self.root_node.value)
        child_count = len(self.root_node.children)
        for i, child in enumerate(self.root_node.children):
            is_last = (i == child_count - 1)
            traverse(child, "", is_last)


# ---------- Example usage ----------

# Create tree structure: A is root, B C D are its children, E and F are B's children
root = TreeNode("A")
tree1 = Tree(root)
child1 = TreeNode("B")
child2 = TreeNode("C")
child3 = TreeNode("D")
root_child1_1 = TreeNode("E")
root_child1_2 = TreeNode("F")
root.add_child(child1)
root.add_child(child2)
root.add_child(child3)
child1.add_child(root_child1_1)
child1.add_child(root_child1_2)

# Print tree in visual form
tree1.print_tree_2d()

# Preorder output: A → B → E → F → C → D
print(tree1.traverse_preorder(root))

# Postorder output: E → F → B → C → D → A
print(tree1.traverse_postorder(root))

# Search for node F
print(tree1.find(root_child1_2))

# Print height from root (should be 2: A → B → E/F)
print(tree1.height(root))

# Count nodes under B (should be 3: B, E, F)
print(tree1.count_nodes(child1))
