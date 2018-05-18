from roguelike.engine.component import Component


class PositionComponent(Component):

    def __init__(self):
        super().__init__(self)

    @property
    def x(self):
        return self._state['x']

    @property
    def y(self):
        return self._state['y']

    @property
    def z(self):
        return self._state['z']
