# =============================================================================
# 🌳 General Tree (N-ary) Using OOP - Outline (with Recursive Node Integration)
# =============================================================================

# -----------------------------------------------------------------------------
# 🔗 Class: TreeNode
# -----------------------------------------------------------------------------
# Purpose:
#   - Represents a single node in the general tree.
#   - Contains:
#       • data     : The value stored in the node.
#       • children : A list of child TreeNode objects (default: empty list).
#   - Acts as the fundamental recursive unit of the general tree.

# (🧩 Write TreeNode class code here)
class TreeNode:
    
    def __init__(self,data):
        self.data = data
        self.children = []
    def is_leaf(self):
        if self.children == []:return "Leaf Node"
        return self.children

# -----------------------------------------------------------------------------
# 🌲 Class: GeneralTree
# -----------------------------------------------------------------------------
# Purpose:
#   - Manages the general tree structure.
#   - Provides methods to add children, search, and traverse.
#   - Uses recursive logic with TreeNode instances internally.
# (🧩 Begin GeneralTree class definition here)


# -----------------------------------------------------------------------------
# 🔐 Attributes:
# -----------------------------------------------------------------------------
#   - __root (private): Refers to the root TreeNode of the tree.


# -----------------------------------------------------------------------------
# 📌 Method: __init__(self)
# -----------------------------------------------------------------------------
# Purpose:
#   - Initializes the tree with an empty root (None).

# (🧩 Write __init__ method here)
class GeneralTree:
    def __init__(self):
        self.__root = None
        self.nodes = []
        self.pre_order = []
        self.post_order = []
# -----------------------------------------------------------------------------
# 📌 Method: add_root(self, data)
# -----------------------------------------------------------------------------
# Purpose:
#   - Sets the root node of the tree.
#   - Only allowed if root is currently None.

# (🧩 Write add_root method here)
    def add_root(self, data):
        if self.is_empty():
            root = TreeNode(data)
            self.__root = root
            print(f"The node, {data} is the root node of the tree.")
            self.nodes.append(self.__root)
        else:
            print(f"The tree already has {self.__root.data} as root")
        

# -----------------------------------------------------------------------------
# 📌 Method: add_child(self, parent_node, data)
# -----------------------------------------------------------------------------
# Purpose:
#   - Adds a child node with given data to the specified parent_node.
#   - Parent node must be a TreeNode in the tree.

# (🧩 Write add_child method here)

    def add_child(self, parent_node, datas):
        if parent_node in self.nodes:
            for data in datas:
                node = TreeNode(data)
                parent_node.children.append(node)
                self.nodes.append(node)
                print(f"As the node,{parent_node.data} is a part of the tree, so its child, {node.data} also become a part of the tree.")
        else:print(f"⚠️ The parent node, {parent_node.data} not a part of the tree.")
# -----------------------------------------------------------------------------
# 📌 Method: search(self, target)
# -----------------------------------------------------------------------------
# Purpose:
#   - Searches for a node containing target data in the tree.
#   - Returns the node if found, else None.

# (🧩 Write search method here)
    def search(self, target):
        for node in self.nodes:
            found = self._search_recursive(node,target)
            if found == None:continue
            else: return True
        return False

# -----------------------------------------------------------------------------
# 📌 Method: _search_recursive(self, current_node, target)
# -----------------------------------------------------------------------------
# Purpose:
#   - Helper method for recursive search.
#   - Checks current node, then recursively searches children.
    def _search_recursive(self, current_node, target):
# 🔹 Step 1: Base case – check if current_node is None.
#   • If there's no node to inspect, return None (end of path or empty tree).
        if current_node == None:return None
        else:
# 🔹 Step 2: Check if current_node.data matches the target.
#   • If it matches, return the current_node (target found).
            if current_node.data == target:return current_node        
# 🔹 Step 3: If not matched, iterate through current_node.children.
#   • Use a loop to check each child recursively.
            else:
                for child in current_node.children:
                    found = self._search_recursive(child,target)
                    if found != None:return found
                
                return None
# 🔹 Step 4: For each child, call _search_recursive(child, target).
#   • Dive deeper into the subtree rooted at each child.

# 🔹 Step 5: After each recursive call, check if a match was found.
#   • If the result is not None, return it immediately (early exit).

# 🔹 Step 6: After all children are searched and no match is found, return None.
#   • This means the target is not in this subtree.


# -----------------------------------------------------------------------------
# 📌 Method: traverse_pre_order(self)
# -----------------------------------------------------------------------------
# Purpose:
#   - To perform a **pre-order traversal** on a general (N-ary) tree.
#   - In pre-order traversal, each node is **visited before** its children.
#   - This creates a **depth-first, top-down** visitation pattern.
#
# Common Use Cases:
#   - Useful when you need to:
#       • Clone a tree structure.
#       • Print a hierarchy (like file systems or organization charts).
#       • Convert a tree into a flat list in top-down order.
#
# -----------------------------------------------------------------------------
# 📚 Step-by-Step Explanation:
# -----------------------------------------------------------------------------
    def traverse_pre_order(self):
# ✅ 1. Check if the tree is empty:
#     - The traversal should start from the root.
#     - If the root is `None`, the tree has no nodes.
#     - In that case, there’s nothing to traverse.
#     - This condition prevents unnecessary recursion or errors.
        if self.is_empty():return ("Tree is empty")
# ✅ 2. Begin traversal from the root node:
#     - If the root exists, initiate the traversal.
#     - This is typically done using a helper method with recursion.
#     - Why recursion? Because a tree is a recursive data structure —
#       each child of a node can itself be treated as a smaller tree.
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

# ✅ 3. Visit the current node (root or child):
#     - The first thing we do is "visit" the node.
#     - Visiting means either:
#         • Printing its data to the console,
#         • Appending the data to a list (for return),
#         • Performing any operation on that node.
#     - This is what makes it **pre-order** — visit first, then children.
#
# ✅ 4. Access the children of the current node:
#     - Each node contains a list (or array) of child nodes.
#     - Use a `for` loop to go through each child in the list.
#     - This introduces the branching behavior of general trees.
            
# ✅ 5. Recursively traverse each child:
#     - For every child in the children list:
#         • Recursively call the same helper method.
#         • The same logic (visit + traverse) will apply to that child.
#     - This recursion ensures that:
#         • We go **deep** into each subtree before returning to siblings.
#         • All nodes are visited in the correct pre-order sequence.
#
# 🔁 6. Continue recursion until all nodes are visited:
#     - Recursion will stop automatically when it hits a leaf node
#       (i.e., a node with no children — its children list is empty).
#     - After completing one child subtree, recursion goes back up
#       to the parent and continues with the next child.
#
# 🧠 Final Result:
#     - All nodes are visited in the order: 
#         • Parent ➜ First child ➜ Subtree of first child ➜ Next child ➜ ...
#     - Produces a natural "outline" of the tree’s hierarchy.
#     - Can be visualized as a top-down depth-first walk through the tree.
#
# Optional Add-on (for advanced use):
#     - You can modify this method to:
#         • Store traversal results in a list and return it.
#         • Accept a callback function to process each node dynamically.
#         • Visualize the tree depth using indentation or tree drawing.


    



# -----------------------------------------------------------------------------
# 📌 Method: traverse_post_order(self)
# -----------------------------------------------------------------------------
# Purpose:
#   - Post-order traversal: recursively traverse children, then visit current node.
#
# Step-by-step Explanation:
#
# 1️⃣ Check if the tree is empty — return "Tree is empty" if so.
# 2️⃣ Define a helper function _post_order_recursive(node)
#     - For each child in node.children:
#         • Recursively call _post_order_recursive(child)
#     - After all children, add current node’s data to result list
# 3️⃣ Call _post_order_recursive(self.__root)
# 4️⃣ Join and return the traversal result string
    def traverse_post_order(self):
        if self.is_empty():return "Tree is empty."
        def _post_order_recursive(node):
            for child in node.children:
                _post_order_recursive(child)
            self.post_order.append(node)
        _post_order_recursive(self.__root)

        visual = " -> ".join(f"{node.data}" for node in self.post_order)
        return f"""------------PostOrder Traversal------------------------
{visual}"""



# -----------------------------------------------------------------------------
# 📌 Method: is_empty(self)
# -----------------------------------------------------------------------------
# Purpose:
#   - Returns True if root is None, else False.

# (🧩 Write is_empty method here)
    def is_empty(self):
        if self.__root == None:return True
        return False
# -----------------------------------------------------------------------------
# 📌 Method: get_root(self)
# -----------------------------------------------------------------------------
# Purpose:
#   - Returns the root node or its data.

# (🧩 Write get_root method here)

    def get_root(self):
        if self.is_empty():return None
        return self.__root
# -----------------------------------------------------------------------------
# 📌 Method: size(self)
# -----------------------------------------------------------------------------
# Purpose:
#   - Returns total number of nodes in the tree.
#   - Uses recursion to count all nodes starting from root.
    def size(self):return self._size_recursive(self.__root)
# (🧩 Write size method here)


# -----------------------------------------------------------------------------
# 📌 Method: _size_recursive(self, node)
# -----------------------------------------------------------------------------
# Purpose:
#   - Helper method to recursively count nodes in a subtree.
#
# Step-by-step Explanation:
    def _size_recursive(self, node):
# 1️⃣ Start with the current node passed as an argument.
#     - This node represents the root of the current subtree being analyzed.
        size = 1
        for child in node.children:
           size += self._size_recursive(child)
        
        return size
# 2️⃣ Initialize a counter to represent the current node.
#     - Since this node exists, count it as 1.
#
# 3️⃣ Loop through each child of the current node.
#     - For every child:
#         • Recursively call `_size_recursive(child)` to count all nodes under that child.
#         • Add the returned count to the current total.
#
# 4️⃣ After all children have been processed,
#     - Return the accumulated total count for this subtree.
#
# 🔁 This recursive process continues upward,
#     aggregating node counts until it reaches the root.

# ----------------------------------------------------------------------------- 
# 📌 Method: remove_node(self, target)
# -----------------------------------------------------------------------------
# Purpose:
# ----------------------------------------------------------------------------- 
# 📌 Method: remove_node(self, target)
# -----------------------------------------------------------------------------
    def remove_node(self, target):
        # 1️⃣ Check if the tree is empty — return a message like "Tree is empty." if so.
        if self.is_empty():
            return "Tree is empty."

        # 2️⃣ Check if the root is the target — remove the entire tree if matched.
        if self.__root.data == target:
            self.__root = None
            self.nodes.clear()
            return f"Root node '{target}' and entire tree removed."

        # 3️⃣ Define a recursive function to find the parent of the target node.
        def find_parent(current_node):
            # 🔹 For each child, check if it matches the target.
            for child in current_node.children:
                if child.data == target:
                    return current_node  # Parent found
                # 🔁 Recurse deeper into the tree
                result = find_parent(child)
                if result:
                    return result
            return None  # Not found in this path

        # 4️⃣ Call the find_parent function starting from the root.
        parent_node = find_parent(self.__root)

        # 5️⃣ If parent found, locate and remove the child and its subtree.
        if parent_node:
            for child in parent_node.children:
                if child.data == target:
                    # 🔁 Define a recursive function to remove the entire subtree.
                    def remove_subtree(node):
                        for sub in node.children:
                            remove_subtree(sub)
                        if node in self.nodes:
                            self.nodes.remove(node)

                    # ❌ Remove the target child from parent's children list.
                    parent_node.children.remove(child)
                    remove_subtree(child)
                    return f"Node '{target}' and its subtree removed."

            return f"Node '{target}' not found under located parent."  # Fallback
        else:
            return f"Node '{target}' not found in the tree."

# ----------------------------------------------------------------------------- 
# 📌 Method: height(self)
# -----------------------------------------------------------------------------
# Purpose:
#   - Calculates and returns the height (maximum depth) of the tree.
#   - Height is defined as number of edges on the longest path from root to a leaf.

    def height(self):
        if self.is_empty():
            return -1  # Conventionally, height of an empty tree is -1

        return self._height_recursive(self.__root)

    # ----------------------------------------------------------------------------- 
    # 📌 Method: _height_recursive(self, node)
    # -----------------------------------------------------------------------------
    # Purpose:
    #   - Helper method to recursively determine the height of a subtree.

    def _height_recursive(self, node):
        if not node.children:
            return 0  # A leaf node has height 0

        # Compute the height of each child and return the maximum + 1
        child_heights = [self._height_recursive(child) for child in node.children]
        return 1 + max(child_heights)



# ----------------------------------------------------------------------------- 
# 📌 Method: clear(self)
# -----------------------------------------------------------------------------
# Purpose:
#   - Clears the entire tree.
#   - Removes all nodes and resets the root to None.
#
# Step-by-step Explanation:
    def clear(self):
# 1️⃣ Check if the tree is empty using is_empty().
#     - If the tree is already empty, return a message like "Tree is already empty."
        if self.is_empty():return "Tree is already empty."
# 2️⃣ Reset the root node to None.
#     - This detaches the entire structure starting from the root.
        else:
            self.__root = None
# 3️⃣ Clear the internal node tracking list (e.g., self.nodes).
#     - This removes all references to TreeNode instances stored in the tree.
            self.nodes.cl# 4️⃣ Clear any traversal-related data structures.
#     - Empty out lists like pre_order, post_order if they exist.
            self.pre_order.clear()
            self.post_order.clear()
# 5️⃣ Return a message indicating the tree has been successfully cleared.
#     - This confirms the operation to the caller.
            print("The tree has been successfully cleared")
            return self.nodes
# 🧠 Final Result:
#     - The tree is fully reset to its initial empty state, with no memory reference to any former nodes.


# ----------------------------------------------------------------------------- 
# 📌 Method: update_node_data(self, target, new_data)
# -----------------------------------------------------------------------------
# Purpose:
#   - Finds the node with the target data.
#   - Updates its data to new_data.
#   - Returns confirmation of update or failure message.
#
# Step-by-step Explanation:
    def update_node_data(self, target, new_data):
        # 1️⃣ Check if the tree is empty — return "Tree is empty." if so.
        if self.is_empty():
            return "Tree is empty."

        # Show pre-order before update
        self.pre_order.clear()
        self.traverse_pre_order()
        print("Traversal (Pre Order) Before Update:")
        visual_before = " -> ".join(f"{node.data}" for node in self.pre_order)
        print(visual_before)

        # 2️⃣ Search for the node and update if found
        found = self._search_recursive(self.get_root(), target)
        if found:
            prev = found.data
            found.data = new_data
            print(f"Node data updated successfully from {prev} to {found.data}.")

            # Show pre-order after update
            self.pre_order.clear()
            self.traverse_pre_order()
            print("Traversal (Pre Order) After Update:")
            visual_after = " -> ".join(f"{node.data}" for node in self.pre_order)
            return visual_after

        # 3️⃣ If not found, return message
        return "Target data not found in the tree."

# 3️⃣ If the target node is found:
#     - Update the node’s data attribute to the new_data value.
#     - Return a success message such as "Node data updated successfully."
#
# 4️⃣ If the target node is not found:
#     - Return a failure message like "Target data not found in the tree."
#
# 🧠 Final Result:
#     - The tree structure remains unchanged, but the specified node's content is updated.
#     - Useful for renaming values or correcting entries without altering the tree shape.



# -----------------------------------------------------------------------------
# 📌 Method: print_tree(self, node=None, level=0)
# -----------------------------------------------------------------------------
# Purpose:
#   - Recursively prints the tree structure in an indented format.
#   - Useful for visualizing the hierarchy and relationships between nodes.
#   - Defaults to printing from the root if no node specified.

    # -----------------------------------------------------------------------------
# 📌 Method: print_tree(self, node=None, level=0)
# -----------------------------------------------------------------------------
# Purpose:
#   - Recursively prints the tree structure in an indented format.
#   - Root node is printed without symbols; children with indentation and "└──".

    def print_tree(self, node=None, level=0):
        # 1️⃣ Check if the tree is empty
        if self.is_empty():
            print("Tree is empty.")
            return

        # 2️⃣ Set the starting node to root if not provided
        if node is None:
            node = self.__root

        # 3️⃣ Print current node
        if level == 0:
            print(f"{str(node.data)} ──> Root")  # No prefix for root
        else:
            print("    " * (level - 1) + "└── " + str(node.data))

        # 4️⃣ Recursively print each child
        for child in node.children:
            self.print_tree(child, level + 1)




# -----------------------------------------------------------------------------
# 🧪 Testing Scenarios
# -----------------------------------------------------------------------------
# ✅ Initialize empty tree and check is_empty().
# ✅ Add root node and verify it is set.
# ✅ Add multiple children to root and other nodes.
# ✅ Search for existing and non-existing values.
# ✅ Perform pre-order and post-order traversals and verify order.
# ✅ Get total size of the tree after inserts.
# ✅ Check behavior when adding child to non-existent parent.
# =============================================================================
tree = GeneralTree()
tree.add_root(5)
root = tree.get_root()
tree.add_child(root,[69,87,56])
node1 = root.children[1]
print(node1.is_leaf())
tree.add_child(node1,[698,857,156])
if tree.search(875):print((f"Found"))
else:print("Not Found")
# # tree.add_child(root,69)
# # tree.traverse_pre_order()
# for node in tree.nodes:print(node.data)
print(tree.traverse_pre_order())
print(tree.traverse_post_order())
print(tree.size())
print(tree._size_recursive(node1))
print(tree.remove_node(857))
print(tree.height())
print(tree.update_node_data(698,69))
tree.print_tree()
print(tree.clear())
print(tree.traverse_pre_order())
print(tree.traverse_post_order())
