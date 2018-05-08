from src.roguelike.game.models.layer import Layer
from src.roguelike.game.models import ElevationKeys


class ElevationLayer(Layer):

    def __init__(self, size, data, thresholds):
        Layer.__init__(size, data, thresholds)
        pass

    def is_ocean(self, x, y):
        return self.get_value(x, y) <= ElevationKeys.SHALLOW_WATER.value

    def is_land(self, x, y):
        return self.get_value(x, y) >= ElevationKeys.COASTAL.value

    def is_mountain(self, x, y):
        return self.get_value(x, y) >= ElevationKeys.MOUNTAIN.value
