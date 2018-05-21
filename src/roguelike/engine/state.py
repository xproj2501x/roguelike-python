class State:

    def __init__(self, name):
        pass
        self._name = name
        self._locked = False
        self._next_state = None

    @property
    def locked(self):
        return self._locked

    @property
    def next_state(self):
        return self._next_state

    def run(self, event):
        self._locked = True

    def enter(self):
        pass

    def exit(self):
        self._locked = False
