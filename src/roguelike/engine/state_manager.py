class StateManager:

    def __init__(self, states, initial_state):
        self._states = states
        self._current_state = self._states[initial_state]

    def update(self, events):
        for event in events:
            if not self._current_state.locked:
                self._current_state.run(event)
            if self._current_state.next_state:
                next_state = self._states[self._current_state.next_state]
                self._current_state.exit()
                self._current_state = next_state
                self._current_state.enter()
                break
