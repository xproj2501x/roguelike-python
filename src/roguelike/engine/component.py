class Component:

    @property
    def entity(self):
        """
        Read only property

        :return: The identity of the parent entity.
        :rtype: int
        """
        return self._entity

    def __init__(self, entity, state):
        """
        :param entity: The identity of the parent entity.
        :type entity: int
        :param state: The initial state of the component
        :type state: dict
        """

        self._entity = entity
        self._state = state

    def update(self, state):
        """
        Updates the component state with new values
        :param state:
        :type state: dict
        """
        for key in state:
            if not self._state[key]:
                raise Exception("Error: Invalid key {0} in state for component.".format(key))
        for key in state:
            self._state[key] = state[key]

    @staticmethod
    def create(entity, state):
        """
        Static factory method.
        :param entity: The identity of the parent entity.
        :type entity: int
        :param state: The initial state of the new component.
        :type state: dict

        :return: A new component instance.
        :rtype: Component
        """
        if not entity:
            raise Exception("Error: Entity id cannot be None.")
        if not state:
            raise Exception("Error: Component state cannot be None.")
        return Component(entity, state)
