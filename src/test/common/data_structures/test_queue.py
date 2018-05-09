import unittest

from src.roguelike.common.data_structures.queue import Queue


class QueueTest(unittest.TestCase):
    """
    Test suite for Queue class.
    """

    def setUp(self):
        self._queue = Queue()

    def test_enqueue(self):
        """
        Test for Queue.enqueue method.
        """
        element = 1
        self._queue.enqueue(element)
        self.assertEquals(self._queue.length, 1)

    def test_dequeue(self):
        """
        Test for Queue.dequeue method.
        """
        element = 1
        self._queue.enqueue(element)
        self._queue.dequeue()
        self.assertEquals(self._queue.length, 0)

    def test_peek(self):
        """
        Test for Queue.peek method.
        """
        element = 1
        self._queue.enqueue(element)
        result = self._queue.peek()
        self.assertEquals(result, element)

    def test_peek_empty(self):
        result = self._queue.peek()
        self.assertEquals(result, False)

    def test_clear(self):
        element = 1
        self._queue.enqueue(element)
        self.assertEquals(self._queue.length, 1)
        self._queue.clear()
        self.assertEquals(self._queue.length, 0)
