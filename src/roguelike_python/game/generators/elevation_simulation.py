class ElevationSimulation:

    def __init__(self, world):
        self._world = world

    def execute(self):
        if self._world.elevation:
            raise Exception('Error: world {0} already contains an elevation layer'.format(self._world.identifier))

    def calculate(self):
        pass