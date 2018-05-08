from roguelike.game.models import DEFAULT_ZONE_SIZE


class Zone:

    def __init__(self, size):
        self._size = size

    @property
    def size(self):
        return self._size

    @staticmethod
    def create(size=None):
        """
        Static factory method
        :param size: The size of the zone. (Default: None)
        :type size: int

        :return: A new zone instance.
        :rtype: Zone
        """
        if not size:
            size = DEFAULT_ZONE_SIZE
        return Zone(size)
