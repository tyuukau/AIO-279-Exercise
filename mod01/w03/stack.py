from typing import Any


class Stack:
    def __init__(self, capacity: int):
        """
        Initializes the stack with a given capacity.

        Args:
            capacity (int): The maximum number of elements the stack can hold.
        """
        self.capacity = capacity
        self.element_stack = []

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.element_stack) == 0

    def is_full(self) -> bool:
        """
        Checks if the stack is full.

        Returns:
            bool: True if the stack is full, False otherwise.
        """
        return len(self.element_stack) == self.capacity

    def pop(self):
        """
        Removes and returns the top element of the stack.

        Returns:
            The top element of the stack if the stack is not empty,
            otherwise returns None.
        """
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        return self.element_stack.pop()

    def push(self, value: Any) -> None:
        """
        Adds a value to the top of the stack.

        Args:
            value: The value to be added to the stack.
        """
        if self.is_full():
            print("Stack is full. Cannot push.")
        else:
            self.element_stack.append(value)

    def top(self) -> Any:
        """
        Returns the top element of the stack without removing it.

        Returns:
            The top element of the stack if the stack is not empty,
            otherwise returns None.
        """
        if self.is_empty():
            print("Stack is empty. No top element.")
            return None
        return self.element_stack[-1]
