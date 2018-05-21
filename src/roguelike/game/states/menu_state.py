from roguelike.engine.state_manager import StateManager
from roguelike.engine.state import State


class MenuState(State):

    def __init__(self):
        super().__init__('MENU')

    def run(self, event):
        super()

    def enter(self):
        pass

    def exit(self):
        super()
