class GraphNode:

    @property
    def id(self):
        return self._key

    @property
    def data(self):
        return self._data

    def __init__(self, key, data):
        self._key = key
        self._data = data
        self._edges = {}

    def add_edge(self, key, weight=0):
        if self._has_edge(key):
            raise Exception("Error: Node {0} already connected to node {1}".format(self._key, key))
        self._edges[key] = weight

    def remove_edge(self, key):
        if not self._has_edge(key):
            raise Exception("Error: Node {0} not connected to node {1}".format(self._key, key))
        del self._edges[key]

    def has_edge(self, key):
        """

        :param key:
        :type key: int

        :return:
        :rtype: bool
        """
        return key in self._edges

    @staticmethod
    def create():
        """
        Static factory method
        :return: A new graph node instance.
        :rtype: GraphNode
        """
        return GraphNode()
