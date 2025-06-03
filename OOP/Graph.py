# -------------------------------
# Node class
# -------------------------------
class Node:
    
    # Constructor to initialize a node with data and neighbors
    def __init__(self, data):
        # self.data : stores the value or identifier of the node
        # self.neighbors : a collection (list or set) of adjacent nodes
        self.data = data
        self.neighbors = []
        
        

    # Add a neighbor node to this node's adjacency list
    def add_neighbor(self, neighbor_node):
        # Append or add neighbor_node to self.neighbors
        self.neighbors.append(neighbor_node)

    # Remove a neighbor node from adjacency list if needed
    def remove_neighbor(self, neighbor_node):
        # Remove neighbor_node from self.neighbors if it exists
        self.neighbors.remove(neighbor_node)

    # String representation for easy debugging
    def __repr__(self):
        # Return string like 'Node(data)'
        return f"Node({self.data})"

# -------------------------------
# Graph class
# -------------------------------
class Graph:
    # Constructor to initialize the graph
    def __init__(self, is_directed=False):
        # self.nodes : dictionary to hold node data -> Node object
        # self.is_directed : boolean flag, True if graph is directed
        self.nodes = {}
        self.is_directed = is_directed
        if self.is_directed == False:print(f"An undirected graph is created")
        else:print(f"A directed graph is created")
        
    



    # Add a node to the graph
    def add_node(self, data):
        # Check if node with data already exists
        # If not, create a new Node and add to self.nodes
        if data in self.nodes:
            print(f"Node containing {data}, is already a part of the graph")
            
        else:
            self.nodes[data] = Node(data)
            print(f"Node containing {data}, is added to the graph")
            print(self.nodes)

    # Add an edge between two nodes
    def add_edge(self, from_data, to_data):
        # If nodes don't exist, optionally create them
        # Add to_data as neighbor of from_data
        # If graph is undirected, also add from_data as neighbor of to_data
        
            if from_data not in self.nodes:
                self.add_node(from_data)
            if to_data not in self.nodes:
                self.add_node(to_data)
            if self.is_directed == True:
                self.nodes[from_data].add_neighbor(self.nodes[to_data])
                print(f"An edge is created from {from_data} to {to_data}")
            else:
                self.nodes[from_data].add_neighbor(self.nodes[to_data])
                self.nodes[to_data].add_neighbor(self.nodes[from_data])
                print(f"2 edges are created from {from_data} to {to_data} and {to_data} to {from_data}")
            
            print(self)
        
            

    # Remove a node and all connected edges from the graph
    def remove_node(self, data):
# -------------------------------
# Method: remove_node
# Purpose: Removes a node and its connections from the graph
# -------------------------------

# Step 1: Check if the node exists in the graph
# We only want to try removing it if it's actually present.
        if self.has_node(data):
# Step 2: Disconnect this node from all other nodes
# Loop through every node in the graph.
# If this node appears in someone else's neighbor list (i.e., connection),
# remove it from that list. This cleans up any links pointing to it.
            for node in self.nodes.values():
                if self.nodes[data] in node.neighbors:
                    node.remove_neighbor(self.nodes[data])
                    print(f"{data} has been removed from the neighbors of {node}")

# Step 3: Remove the node from the graph dictionary
# Once it's disconnected, we safely delete the node itself from the main graph.
            self.nodes.pop(data)
            print(f"{data} has been removed from the graph")
            print(self)
# Step 4 (Optional): Print a confirmation message
# Let the user know that the node was successfully removed.

          
        
        

    # Remove an edge between two nodes
    def remove_edge(self, from_data, to_data):
        # Remove to_data from from_data neighbors
        if self.is_directed == False:self.nodes[to_data].remove_neighbor(self.nodes[from_data])
        self.nodes[from_data].remove_neighbor(self.nodes[to_data])
        print(f"There is no connection remained between {from_data} and {to_data}")
        print(self)
        # If undirected, also remove from_data from to_data neighbors
        

    # Check if a node exists in the graph
    def has_node(self, data):
        # Return True if data is in self.nodes keys, else False
        if data in self.nodes:return True
        return False
        

    # Check if an edge exists between two nodes
    def has_edge(self, from_data, to_data):
        # Return True if to_data is in from_data neighbors, else False
        if self.nodes[to_data] in self.nodes[from_data].neighbors:
            if self.is_directed:print(f"There is an edge between {from_data} and {to_data}")
            else:print(f"There are 2 edges between {from_data} and {to_data}")
            return True
        print(f"There are no edges between {from_data} and {to_data}")
        return False

    # Get all neighbors of a given node
    def get_neighbors(self, data):
        # Return list or set of neighbors for the node with data
        return self.nodes[data].neighbors

    # Breadth-First Search (BFS) traversal from a start node
    def bfs(self, start_data):
            # -------------------------------
        if start_data in self.nodes:
            visited = []
            queue = [start_data]  # Start with a string

            while queue:
                current_data = queue.pop(0)
                if current_data not in visited:
                    visited.append(current_data)
                    for neighbor_node in self.nodes[current_data].neighbors:
                        if neighbor_node.data not in visited:
                            queue.append(neighbor_node.data)

            print(f"BFS traversal of {start_data}")
            visual = "->".join(f"{node}"for node in visited)
            return visual
        else:
            return f"{start_data} not a part of graph. So no need for BFS traversal"
        
    # Depth-First Search (DFS) traversal from a start node
    def dfs(self, start_data):
        # Step 1: Check if the start node exists in the graph
        if start_data not in self.nodes:
            print(f"Start node '{start_data}' not found in the graph.")
            return

        visited = set()  # To keep track of visited nodes
        result = []      # To store the DFS traversal order

        # Step 2: Define a recursive helper function for DFS
        def dfs_recursive(node):
            visited.add(node.data)       # Mark the current node as visited
            result.append(node.data)     # Store the visited node
            for neighbor in node.neighbors:
                if neighbor.data not in visited:
                    dfs_recursive(neighbor)  # Visit unvisited neighbor

        # Step 3: Start DFS from the given start_data node
        dfs_recursive(self.nodes[start_data])

        # Step 4: Print the final DFS order
        print("DFS Traversal:", " → ".join(result))


    # String representation of the graph
    def __repr__(self):
        # Return string showing nodes and their adjacency lists
        result = []
        for key, node in self.nodes.items():
            neighbors = [neighbor.data for neighbor in node.neighbors]
            result.append(f"{key}: {neighbors}")
        return "\n".join(result)

# -------------------------------
# Example Usage
# -------------------------------

# 1. Create a graph object (directed or undirected)
graph = Graph(is_directed=False)

# 2. Add nodes
graph.add_node("A")
graph.add_node("B")

# 3. Add edges
graph.add_edge("A", "B")
graph.add_edge("B", "C")

print(graph.has_edge("A", "C"))


# 4. Remove nodes as needed
graph.remove_node("C")

# 4. Remove edges as needed
graph.remove_edge("A", "B")

graph.add_edge("A", "D")
graph.add_edge("B", "D")
graph.add_edge("A", "F")
graph.add_edge("B", "E")

print(graph.get_neighbors("A"))
# # 6. Traverse graph
print(graph.bfs("A")) #A → D → F → B → E
graph.dfs("A") #A → D → B → E → F


# # 7. Check existence of nodes or edges
# print(graph.has_node("C")) #-> True
# graph.has_edge("A", "B") #-> False after removal
