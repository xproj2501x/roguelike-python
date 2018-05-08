from src.roguelike_python.game.models import PrecipitationKeys
from src.roguelike_python.game.models.layer import Layer


class PrecipitationLayer(Layer):

    def __init__(self, size, data, thresholds):
        Layer.__init__(size, data, thresholds)
        pass

    def is_arid(self, x, y):
        return self.get_value(x, y) == PrecipitationKeys.ARID.value
