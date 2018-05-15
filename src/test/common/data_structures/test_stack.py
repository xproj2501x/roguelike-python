import unittest

from src.roguelike.common.data_structures.stack import Stack


class StackTest(unittest.TestCase):

    def setUp(self):
        self._stack = Stack()

    def test_push(self):
        """
        Test for Stack.push method.
        """
        element = 1
        self._stack.push(element)
        self.assertEquals(self._stack.length, 1)

    def test_pop(self):
        """
        Test for Stack.pop method.
        """
        element = 1
        self._stack.push(element)
        self._stack.pop()
        self.assertEquals(self._stack.length, 0)

    def test_peek(self):
        """
        Test for Stack.peek method.
        """
        element = 1
        self._stack.push(element)
        result = self._stack.peek()
        self.assertEquals(result, element)

    def test_peek_empty(self):
        """
        Test for Stack.peek method.
        """
        result = self._stack.peek()
        self.assertEquals(result, False)

    def test_clear(self):
        """
        Test for Stack.clear method.
        """
        element = 1
        self._stack.push(element)
        self.assertEquals(self._stack.length, 1)
        self._stack.clear()
        self.assertEquals(self._stack.length, 0)
