from roguelike.engine.component import Component


class VelocityComponent(Component):

    def __init__(self, entity, state):
        super().__init__(entity, state)

    @property
    def dx(self):
        return self._state['dx']

    @property
    def dy(self):
        return self._state['dy']

    @property
    def dz(self):
        return self._state['dz']
