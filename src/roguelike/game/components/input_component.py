from roguelike.engine.component import Component


class InputComponent(Component):

    def __init__(self, entity, state):
        super().__init__(entity, state)
