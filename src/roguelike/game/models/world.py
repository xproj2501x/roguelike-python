import uuid

from src.roguelike.game.models import DEFAULT_WORLD_SIZE, LayerName


class World:

    def __init__(self, identity, size):
        self._identity = identity
        self._size = size
        self._layers = []

    @property
    def identityr(self):
        return self._identity

    @property
    def size(self):
        return self._size

    @property
    def elevation(self):
        return self._layers[LayerName.ELEVATION.value]

    @property
    def temperature(self):
        return self._layers[LayerName.TEMPERATURE.value]

    @property
    def precipitation(self):
        return self._layers[LayerName.PRECIPITATION.value]

    @staticmethod
    def create(identity=None, size=None):
        """
        Static factory method.
        :param identity: The identifier for the new world. (Default: None)
        :type identity: UUID
        :param size: The size of the world. (Default: None)
        :type size: int

        :return: A new world instance.
        :rtype: World
        """
        if not identity:
            identity= uuid.uuid4()
        if not size:
            size = DEFAULT_WORLD_SIZE
        return World(identity, size)
