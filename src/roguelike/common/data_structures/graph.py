from src.roguelike.common.data_structures.graph_node import GraphNode


class Graph:

    def __init__(self):
        self._nodes = {}

    def __len__(self):
        return len(self._nodes)

    def __contains__(self, key):
        if self.get_node(key):
            return True
        return False

    def add_node(self, key, data):
        if self._has_node(key):
            raise Exception("Error: Node id {0} already exists in the graph".format(key))
        node = GraphNode(key, data)
        self._nodes[key] = node

    def get_node(self, key):
        if not self._has_node(key):
            raise Exception("Error: Node id {0} does not exist in the graph".format(key))
        return self._nodes[key]

    def remove_node(self, key):
        if not self._has_node(key):
            raise Exception("Error: Node id {0} does not exist in the graph".format(key))
        node = self._nodes[key]

        del self._nodes[key]

    def add_edge(self, node1_key, node2_key, weight):
        """

        :param node1_key:
        :type node1_key:
        :param node2_key:
        :type node2_key:
        :param weight:
        :type weight:

        :return:
        :rtype:
        """
        if not self._has_node(node2_key):
            raise Exception("Error: Node id {0} does not exist in the graph".format(node2_key))
        node = self.get_node(node1_key)
        node.add_edge(node2_key, weight)

    def remove_edge(self, node1_key, node2_key):
        node = self.get_node(node1_key)
        node.remove_edge(node2_key)

    def _has_node(self, key):
        return key in self._node

    def _has_edge(self, node1_key, node2_key):
        """

        :param node1_key:
        :param node2_key:

        :return:
        :rtype: bool
        """
        node = self.get_node(node1_key)
        return node.has_edge(node2_key)

    @staticmethod
    def create():
        return Graph()
