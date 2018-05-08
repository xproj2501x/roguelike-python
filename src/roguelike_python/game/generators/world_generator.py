from src.roguelike_python.common.algorithms.diamond_square_height_map import DiamondSquareHeightMap
from src.roguelike_python.game.models.world import World


class WorldGenerator:

    def __init__(self):
        self._world = None
        self._diamond_square_height_map = DiamondSquareHeightMap()

    def build(self, size=None):
        """
        Builds a new World instance.
        :param size: The size of the world to be built. (Default: None)
        :type size: int

        :return: The generated World instance.
        :rtype: World
        """
        self._world = World.create(size=size)
        layer = self._diamond_square_height_map.generate(self._world.size)

    def _run_step(self, name):
        pass

    @staticmethod
    def create():
        """
        Static factory method

        :return: A new WorldGenerator instance
        :rtype: WorldGenerator
        """
        return WorldGenerator()
