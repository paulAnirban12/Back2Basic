# Queue class: Implements FIFO (First-In-First-Out) structure
class Queue:
    def __init__(self, max_size=None):
        # Initialize queue list and optional max size
        self.queue = []
        self.max_size = max_size
        if self.max_size != None:
            print(f"A queue is created with the space for {self.max_size} items!")
        else:
            print(f"A queue is created!")

    def __str__(self):
        # Return a visual string of the queue or "Empty Queue" if it's empty
        if not self.queue:
            return "Empty Queue."
        else:
            visual = " ".join(f"[{item}]" for item in self.queue)
            front_marker = "First ->"
            rear_marker = "<- Last"
            return f"{front_marker} {visual} {rear_marker}"

    def enqueue(self, item):
        # Add item at the rear if queue is not full
        if self.is_full():
            print("Queue is full.")
        else:
            self.queue.append(item)
            if self.max_size != None:
                slots = self.max_size - self.size()
                print(f"{item} has been inserted successfully to the queue with {slots} slots remaining.")
            else:
                print(f"{item} has been pushed successfully to the stack.")
            print(self)

    def dequeue(self):
        # Remove item from front if not empty
        removed_item = self.queue.pop(0)
        print(f"{removed_item} has been removed from the queue.")
        if self.is_empty():
            print(f"After removing {removed_item}, the queue gets empty!")
        else:
            print(self)

    def is_empty(self):
        # Check if queue is empty
        return self.size() == 0

    def is_full(self):
        # Check if queue has reached max size
        if self.max_size != None:
            return self.size() >= self.max_size
        else:
            return False

    def peek(self):
        # Show front item without removing it
        if self.is_empty():
            print("The stack is empty")
        else:
            print(self.queue[0])

    def size(self):
        # Return number of elements in queue
        return len(self.queue)


# Testing the Queue class
queue = Queue(10)       # Create a queue with a capacity of 10
queue.enqueue(67)       # Add 67 to the queue
queue.enqueue(79)       # Add 79 to the queue
queue.peek()            # View the front item (should be 67)
