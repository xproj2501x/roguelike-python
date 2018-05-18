from roguelike.engine.system import System

MAX_LENGTH = 64
MULTIPLIER = 0x5D588B656C078965
ADDEND = 0x0000000000269EC3


class PRNGSystem(System):

    def __init__(self):
        super().__init__()

    def update(self):
        pass
