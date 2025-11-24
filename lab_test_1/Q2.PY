import timeit
from typing import Any, Optional, List

# --- SECTION 1: FEW-SHOT PROMPT DESIGN FOR AI CODE GENERATION ---
# This is the prompt designed to guide a model (like Gemini) to produce the
# correct, self-contained Python code for a singly linked list.

FEW_SHOT_PROMPT = """
You are an expert Python programmer specializing in data structures.
Your task is to write a complete, self-contained Python script for a basic 
Singly Linked List implementation. The code must include two classes: 
'Node' and 'LinkedList'.

The 'LinkedList' class must implement the following two methods exactly:
1. 'insert_at_end(data)': Inserts a new node with the given data at the end of the list.
2. 'delete_by_value(value)': Searches for the first occurrence of the given value and removes that node.

All output must be executable Python code enclosed in a single code block. Do not include any explanatory text outside of the code block.

--- FEW-SHOT EXAMPLES ---

# SHOT 1: Basic Node Class
# Input: Write the Node class.
# Output:
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# SHOT 2: Basic Initialization
# Input: Write the structure for the LinkedList class initialization.
# Output:
class LinkedList:
    def __init__(self):
        self.head = None

# SHOT 3: Traversal Example (Helper)
# Input: Write a method to print the list.
# Output:
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

--- END EXAMPLES ---

Now, generate the complete, final Python code containing the 'Node', 'LinkedList', 
'insert_at_end', and 'delete_by_value' methods, along with the 'print_list' method
and a testing block for demonstration.
"""

# --- SECTION 2: SIMULATED AI-GENERATED CODE (LINKED LIST IMPLEMENTATION) ---
# This is the expected output from the AI based on the few-shot prompt above.

class Node:
    """Represents a single node in the Linked List."""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    """
    A basic implementation of a Singly Linked List with common operations.
    
    """
    def __init__(self):
        self.head = None

    def print_list(self):
        """Prints the entire list contents from head to tail."""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

    def insert_at_end(self, data: Any):
        """
        Inserts a new node containing the given data at the end of the list.
        Time Complexity: O(n) in the worst case (needs to traverse the list).
        """
        new_node = Node(data)
        
        # 1. If the list is empty, make the new node the head
        if self.head is None:
            self.head = new_node
            return

        # 2. Traverse to the last node
        last = self.head
        while last.next:
            last = last.next
            
        # 3. Change the next pointer of the last node
        last.next = new_node

    def delete_by_value(self, value: Any) -> bool:
        """
        Searches for the first occurrence of a value and removes that node.
        Returns True if deletion was successful, False otherwise.
        Time Complexity: O(n) in the worst case (needs to traverse the entire list).
        """
        current = self.head
        
        # Case 1: The head node itself holds the value
        if current is not None and current.data == value:
            self.head = current.next  # Move head to the next node
            current = None  # Free the old head node
            return True

        # Case 2: Search for the value, keeping track of the previous node
        prev = None
        while current is not None and current.data != value:
            prev = current
            current = current.next

        # Case 3: Value was not present in the list
        if current is None:
            return False

        # Case 4: Value is found and node is not the head (prev is not None)
        # Unlink the node from the linked list by setting the previous node's next
        # pointer to the current node's next pointer.
        prev.next = current.next
        current = None # Free the node
        return True

# --- SECTION 3: ANALYSIS, TESTING, AND USER INTERACTION ---

def get_list_input() -> List[Any]:
    """Prompts the user for elements to build the initial linked list."""
    while True:
        try:
            user_input = input("Enter 3-5 initial elements for the list (comma-separated, e.g., A, B, C): ")
            if not user_input.strip():
                 # Default list if user provides no input
                return ["Mercury", "Venus", "Earth", "Mars"] 
            
            elements = [item.strip() for item in user_input.split(',')]
            if len(elements) < 1:
                print("Please enter at least one element.")
                continue
            return elements
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

def get_delete_input(current_list_elements: List[Any]) -> Any:
    """Prompts the user for the value to delete."""
    print(f"\nCurrent List Elements: {current_list_elements}")
    value = input("Enter the value to DELETE from the list (must match one of the elements above): ")
    return value.strip()


if __name__ == "__main__":
    print(f"--- Few-Shot Prompt Analysis and Testing ---")
    print("The goal of the few-shot prompt was to generate the following classes:")
    print("Node, LinkedList (with insert_at_end and delete_by_value methods).")
    
    # 1. Initialize the Linked List based on user input
    initial_elements = get_list_input()
    ll = LinkedList()
    
    print("\n--- Linked List Construction (Using insert_at_end) ---")
    for element in initial_elements:
        ll.insert_at_end(element)
        print(f"Inserted: {element}")
    
    print("\nInitial List Status:")
    ll.print_list()

    # 2. Test Deletion based on user input
    value_to_delete = get_delete_input(initial_elements)
    
    print(f"\nAttempting to delete first occurrence of: '{value_to_delete}'")
    success = ll.delete_by_value(value_to_delete)
    
    # 3. Test for Correctness and Completeness
    print("\n--- Code Correctness and Completeness Check ---")
    
    if success:
        print(f"SUCCESS: Node with value '{value_to_delete}' was deleted.")
    else:
        print(f"FAILURE: Node with value '{value_to_delete}' was NOT found or deleted.")
    
    print("Final List Status after Deletion:")
    ll.print_list()
    
    print("\nCode Analysis Summary:")
    print("1. Correctness: The generated Node and LinkedList classes correctly handle head and next pointers.")
    print("2. Completeness: All required methods (`insert_at_end`, `delete_by_value`, `Node`) were implemented.")
    print("3. Robustness: The `delete_by_value` method correctly handles three critical cases:")
    print("   a) Deleting the head node.")
    print("   b) Deleting a node in the middle/end.")
    print("   c) Value not found (traverses to the end and returns False).")