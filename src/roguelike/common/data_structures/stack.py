class Stack:

    def __init__(self):
        self._data = []

    @property
    def length(self):
        return len(self._data)

    def push(self, element):
        """
        Adds an element to the top of the stack.
        :param element: The element to be added.
        :type element: object
        """
        self._data.append(element)

    def pop(self):
        """
        Pops an element off the top of the stack.

        :return: The popped element.
        :rtype: object
        """
        return self._data.pop()

    def peek(self):
        """
        Returns the first element on the queue if available, otherwise returns false

        :return: the first element in the queue
        :rtype: object
        """
        if self.length:
            return self._data[0]
        else:
            return False

    def clear(self):
        self._data = []

    @staticmethod
    def create():
        """
        Static factory method.

        :return: A new stack instance.
        :rtype: Stack
        """
        return Stack()
