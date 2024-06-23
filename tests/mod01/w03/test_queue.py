import unittest

from mod01.w03.queue import Queue


class TestQueue(unittest.TestCase):

    def test_initialisation(self):
        """
        Test if the queue initializes with the correct capacity and is empty.
        """
        queue = Queue(capacity=3)
        self.assertEqual(queue.capacity, 3)
        self.assertTrue(queue.is_empty())
        self.assertFalse(queue.is_full())
        self.assertEqual(queue.element_queue, [])

    def test_is_empty(self):
        """
        Test if the queue is initially empty.
        """
        queue = Queue(capacity=3)
        self.assertTrue(queue.is_empty())
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())

    def test_is_full(self):
        """
        Test if the queue correctly identifies when it is full.
        """
        queue = Queue(capacity=3)
        self.assertFalse(queue.is_full())
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertTrue(queue.is_full())

    def test_enqueue(self):
        """
        Test enqueuing elements into the queue.
        """
        queue = Queue(capacity=3)
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.element_queue, [1, 2])
        queue.enqueue(3)
        self.assertTrue(queue.is_full())
        # Attempt to enqueue when full
        queue.enqueue(4)
        self.assertEqual(queue.element_queue, [1, 2, 3])

    def test_dequeue(self):
        """
        Test dequeuing elements from the queue.
        """
        queue = Queue(capacity=3)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.element_queue, [2, 3])
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        # Dequeue from empty queue
        self.assertIsNone(queue.dequeue())

    def test_front(self):
        """
        Test accessing the front element of the queue.
        """
        queue = Queue(capacity=3)
        self.assertIsNone(queue.front())
        queue.enqueue(1)
        self.assertEqual(queue.front(), 1)
        queue.enqueue(2)
        self.assertEqual(queue.front(), 1)
        queue.dequeue()
        self.assertEqual(queue.front(), 2)


if __name__ == "__main__":
    unittest.main()
