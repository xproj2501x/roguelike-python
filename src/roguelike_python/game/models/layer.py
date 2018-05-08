class Layer:

    def __init__(self, size, data, thresholds):
        self._size = size
        self._data = data
        self._thresholds = thresholds

    def get_raw_value(self, x, y):
        """
        Returns the raw value
        :param x:
        :type x: int
        :param y:
        :type y: int

        :return:
        :rtype: float
        """
        return self._data[x + (y * self._size)]

    def get_value(self, x, y):
        raw_value = self.get_raw_value(x, y)
        for index in range(len(self._thresholds)):
            if raw_value <= self._thresholds[index]:
                return index

    @staticmethod
    def create(size, data, thresholds):
        """
        Static factory method.
        :param size: The size of the layer.
        :type size: int
        :param data:
        :type data: list
        :param thresholds:
        :type thresholds: dict

        :return: A new layer instance.
        :rtype: Layer
        """
        return Layer(size, data, thresholds)
