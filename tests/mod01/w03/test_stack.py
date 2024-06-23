import unittest

from mod01.w03.stack import Stack


class TestStack(unittest.TestCase):

    def test_stack_initialization(self):
        stack = Stack(3)
        self.assertEqual(stack.capacity, 3)
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())

    def test_push_to_stack(self):
        stack = Stack(3)
        stack.push(1)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.top(), 1)
        stack.push(2)
        self.assertEqual(stack.top(), 2)
        stack.push(3)
        self.assertTrue(stack.is_full())

        # Trying to push to a full stack
        stack.push(4)
        self.assertEqual(stack.top(), 3)

    def test_pop_from_stack(self):
        stack = Stack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.is_empty())

        # Trying to pop from an empty stack
        self.assertIsNone(stack.pop())

    def test_top_element(self):
        stack = Stack(3)
        self.assertIsNone(stack.top())
        stack.push(1)
        self.assertEqual(stack.top(), 1)
        stack.push(2)
        self.assertEqual(stack.top(), 2)
        stack.pop()
        self.assertEqual(stack.top(), 1)

    def test_is_empty_and_is_full(self):
        stack = Stack(2)
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        stack.push(1)
        self.assertFalse(stack.is_empty())
        stack.push(2)
        self.assertTrue(stack.is_full())


if __name__ == "__main__":
    unittest.main()
