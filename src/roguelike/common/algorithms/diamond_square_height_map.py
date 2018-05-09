import math
import random


class DiamondSquareHeightMap:

    def __init__(self):
        self._size = None
        self._map = None

    def generate(self, size, roughness=None, seed=None):
        """

        :param size:
        :type size: int
        :param roughness:
        :type roughness: float
        :param seed:
        :type seed: float

        :return:
        :rtype: list
        """
        self._size = size
        self._map = [None] * (self._size * self._size)
        if not roughness:
            roughness = random.random()
        if not seed:
            seed = random.random()
        self._set_cell(0, 0, seed)
        self._set_cell(0, self._size - 1, seed)
        self._set_cell(self._size - 1, self._size - 1, seed)
        self._set_cell(self._size - 1, 0, seed)
        side = self._size - 1
        deviation = roughness
        while side >= 2:
            self._run_square_step(side, deviation)
            self._run_diamond_step(side, deviation)
            deviation *= roughness
            side = int(math.floor(side / 2))
        return self._map

    def _get_cell(self, x, y):
        """
        Returns the value for the cell at the specified position.
        :param x: The x position of the cell.
        :type x: int
        :param y: The y position of the cell.
        :type y: int

        :return: The value of the cell
        :rtype: float
        """
        return self._map[x + (y * self._size)]

    def _set_cell(self, x, y, value):
        """
        Sets the value for the cell at the specified position if it is not already set.
        :param x: The x position of the cell.
        :type x: int
        :param y: The y position of the cell.
        :type y: int
        :param value: The value of the cell.
        :type value: float
        """
        position = x + (y * self._size)
        self._map[position] = self._map[position] if self._map[position] else value

    def _run_square_step(self, side, deviation):
        """

        :param side:
        :type side: int
        :param deviation:
        :type deviation: float
        """
        half_side = int(math.floor(side / 2))
        for x in range(0, self._size - 1, side):
            for y in range(0, self._size - 1, side):
                height = self._calculate_height([
                    [x, y],
                    [x + side, y + side],
                    [x + side, y],
                    [x, y + side]
                ], deviation)
                self._set_cell(x + half_side, y + half_side, height)

    def _run_diamond_step(self, side, deviation):
        """

        :param side:
        :type side: int
        :param deviation:
        :type deviation: float
        """
        half_side = int(math.floor(side / 2))
        for x in range(0, self._size, half_side):
            for y in range((x + half_side) % side, self._size, side):
                height = self._calculate_height([
                    [x, y + half_side],
                    [x + half_side, y],
                    [x - half_side, y],
                    [x, y - half_side]
                ], deviation)
                self._set_cell(x, y, height)

    def _calculate_height(self, cells, height):
        total = 0
        count = 0
        for cell in cells:
            if cell[0] >= 0 and cell[1] >= 0:
                if cell[0] < self._size and cell[1] < self._size:
                    total += self._get_cell(cell[0], cell[1])
                    count += 1
        average = total / count
        return average + random.normalvariate(0, height)

    def _scale_map(self):
        largest = float('-inf')
        smallest = float('inf')
        for x in range(len(self._map)):
            if x > largest:
                largest = x
            if x < smallest:
                smallest = x
        delta = largest - smallest
        scaled = (self._map - smallest) / delta
        return scaled

    @staticmethod
    def create():
        """
        Static factory method

        :return: A new diamond square height map instance.
        :rtype: DiamondSquareHeightMap
        """
        return DiamondSquareHeightMap()
