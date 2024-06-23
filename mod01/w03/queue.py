from typing import Any


class Queue:
    def __init__(self, capacity: int):
        """
        Initializes the queue with a given capacity.

        Args:
            capacity (int): The maximum number of elements the queue can hold.
        """
        self.capacity = capacity
        self.element_queue = []

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.element_queue) == 0

    def is_full(self) -> bool:
        """
        Checks if the queue is full.

        Returns:
            bool: True if the queue is full, False otherwise.
        """
        return len(self.element_queue) == self.capacity

    def dequeue(self):
        """
        Removes and returns the first element of the queue.

        Returns:
            The first element of the queue if the queue is not empty,
            otherwise returns None.
        """
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        return self.element_queue.pop(0)

    def enqueue(self, value: Any) -> None:
        """
        Adds a value to the end of the queue.

        Args:
            value: The value to be added to the queue.
        """
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
        else:
            self.element_queue.append(value)

    def front(self):
        """
        Returns the first element of the queue without removing it.

        Returns:
            The first element of the queue if the queue is not empty,
            otherwise returns None.
        """
        if self.is_empty():
            print("Queue is empty. No front element.")
            return None
        return self.element_queue[0]
