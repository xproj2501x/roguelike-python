import random

from src.roguelike.game.models.layer import Layer


class PrecipitationSimulation:

    def __init__(self, world):
        self._world = world

    def execute(self):
        if self._world.precipitation:
            raise Exception("Error: World {0} already contains a precipitation layer".format(self._world.identity))

    def calculate_thresholds(self):
        pass
