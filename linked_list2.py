class Node:
    """A single node in a doubly linked list."""

    def __init__(self, value):
        self.value = value   # The data this node holds
        self.next = None     # Reference to the next node (None if this is the last item)
        self.prev = None     # Reference to the previous node (None, if this is the first item)

    def __repr__(self):
        return f"Node({self.value})"

class LinkedList:
    """A doubly linked list."""

    def __init__(self):
        self.head = None  # The list starts empty
        self.tail = None # Keep track of the tail for easy backward access

    def insert_at_beginning(self, value):
        """Add a new node at the front of the list. O(1) time."""
        new_node = Node(value)
        if self.head is None:  # if list is empty, head and tail both point to the new node
            self.head = new_node    # New node becomes the new head
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def insert_at_end(self, value):
        """Add a new node at the end of the list. O(n) time - must traverse to the end."""
        new_node = Node(value)
        if self.head is None:    # if List is empty
            self.head = new_node
            self.tail = new_node # New node is now the tail
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node # New node is now the tail


    def search(self, target):
        """Find a value in the list. Returns True/False. O(n) time"""
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next  # Follow the pointer to the next node
        return False


    def display(self):
        """Print the list in a readable format. Prints the list forward (head to tail)."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" <-> ".join(elements) + " <-> None")


    def display_reverse(self):
        """Print the list backward (from tail to head) without converting to a list."""
        elements = []
        current = self.tail # Start at the end (tail).
        while current:
            elements.append(str(current.value))
            current = current.prev # Move backward through the list.
        print(" <-> ".join(elements) + " <-> None")

    def delete(self, target):
        """Remove the first node with the given value. Return True if found, False if not."""
        if self.head is None:
            return False

        current = self.head
        while current:
            if current.value == target:
                # Case 1: Node to delete is the head
                if current == self.head:
                    self.head = self.head.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None # List is now empty

                # Case 2: Node to delete is the tail
                elif current == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None

                # Case 3: Node is somewhere in the middle
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                return True
            current = current.next
        return False


    def length(self):
        """Return the number of nodes in the list. O(n) time."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def to_list(self):
        """Convert the linked list to a Python list. Returns a list of values."""
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements

def is_balanced(text):
        """Return True if all brackets in text are properly matched. Handles: (), [], {}"""

        stack = []
        matching_bracket = {")": "(", "]": "[", "}": "{"}

        for char in text:
            if char in matching_bracket.values():
                stack.append(char)
            elif char in matching_bracket.keys():
                # If stack is empty or top of stack doesn't match the opening pair
                if not stack or stack.pop() != matching_bracket[char]:
                    return False

        # If stack is empty, all brackets matched successfully
        return len(stack) == 0


# Testing the Doubly Linked list
my_list = LinkedList()
my_list.insert_at_beginning(3)
my_list.insert_at_beginning(2)
my_list.insert_at_beginning(1)
my_list.insert_at_end(4)


print(my_list.search(3))  # True
print(my_list.search(99)) # False


# A stack is just a list where you only use append() and pop()
stack = []
stack.append("page_1")   # Push: visit page 1
stack.append("page_2")   # Push: visit page 2
stack.append("page_3")   # Push: visit page 3

print(stack)        # ['page_1', 'page_2', 'page_3']

back = stack.pop()   # Pop: go back
print(back)     # 'page_3' - the most recent page
print(stack)    # ['page_1', 'page_2']


from collections import deque

queue = deque()
queue.append("customer_1")  # Enqueue: customer 1 joins the line
queue.append("customer_2")  # Enqueue: customer 2 joins the line
queue.append("customer_3")  # Enqueue: customer 3 joins the line

print(queue)    # deque(['customer_1', 'customer_2', 'customer_3'])

served = queue.popleft()   # dequeue: serve the first customer
print(served)        #'customer_1' - first in, first out
print(queue)        # dequeue(['customer_2', 'customer_3'])



from collections import deque


class TaskProcessor:
    """Simulates a task processor using a queue."""
    def __init__(self):
        self.tasks = deque()

    def add_task(self, name):
        """Add a task to the queue."""
        self.tasks.append(name)

    def process_next(self):
        """Return the oldest unprocessed task (FIFO) or None if empty."""
        if len(self.tasks) > 0:
            return self.tasks.popleft()
        return None


# Tests:

print("Forward Display:")
my_list.display()     # Output: 1 <-> 2 <-> 3 <-> 4 <-> None

print("Reverse Display (using prev pointers):")
my_list.display_reverse()   # Output: 4 <-> 3 <-> 2 <-> 1 <-> None

print(my_list.search(3))  # True
print(my_list.search(99)) # False

# Stack validator test
print(is_balanced("()"))      # True
print(is_balanced("({[]})"))  # True
print(is_balanced("(]"))      # False
print(is_balanced("([)]"))    # False
print(is_balanced("hello (world)"))  # True