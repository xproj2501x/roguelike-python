import random

from src.roguelike.game.models.layer import Layer


class ElevationSimulation:

    def __init__(self, world, diamond_square_height_map):
        self._world = world
        self._ocean_level = None
        self._diamond_square_height_map = diamond_square_height_map

    def execute(self):
        if self._world.elevation:
            raise Exception("Error: World {0} already contains an elevation layer".format(self._world.identity))
        self._ocean_level = random.uniform(0.5, 0.75)
        roughness = random.uniform(0.5, 7.5)
        seed = random.uniform(self._ocean_level, 0.05)
        map = self._diamond_square_height_map.generate(self._world.size, roughness, seed)

    def calculate_thresholds(self):
        pass
