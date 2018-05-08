import uuid

from src.roguelike_python.game.models import DEFAULT_WORLD_SIZE, LayerName


class World:

    def __init__(self, identifier, size):
        self._identifier = identifier
        self._size = size
        self._layers = []

    @property
    def identifier(self):
        return self._identifier

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
    def create(identifier=None, size=None):
        """
        Static factory method
        :param identifier: The identifier for the new world.
        :type identifier: UUID
        :param size: The size of the world.
        :type size: int

        :return: A new World instance.
        :rtype: World
        """
        if not identifier:
            identifier = uuid.uuid4()
        if not size:
            size = DEFAULT_WORLD_SIZE
        return World(identifier, size)
