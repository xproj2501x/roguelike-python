class ElevationSimulation:

    def __init__(self, world):
        self._world = world

    def execute(self):
        if self._world.elevation:
            raise Exception('Error: World {0} already contains an elevation layer'.format(self._world.identity))
        self._ocean_level = 'foo'

    def calculate(self):
        pass