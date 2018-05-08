from engine import MAX_ENTITIES
from engine.component import Component


class ComponentManager:

    def __init__(self):
        """

        """
        self._components = [None] * MAX_ENTITIES
        self._component_type = 1

    def create_component(self, entity, state):
        """
        Creates a new instance of component.
        :param entity: The identity of the parent entity.
        :type entity: int
        :param state:
        :type state: dict
        """
        if self.has_component(entity):
            raise Exception("Error: Component type {0} for entity id {1} already exists."
                            .format(self._component_type, entity))
        component = Component.create(entity, state)
        self._components[entity] = component

    def destroy_component(self, entity):
        """

        :param entity: The identity of the parent entity.
        :type entity: int
        """
        if not self.has_component(entity):
            raise Exception("Error: Component type {0} for entity id {1} does not exist."
                            .format(self._component_type, entity))
        components = self._components[self._component_type]
        del components[entity]

    def update_component(self, entity, state):
        """

        :param entity: The identity of the parent entity.
        :type entity: int
        :param state:
        :type state: dict
        """
        component = self.get_component[entity]
        component.update(state)

    def get_component(self, entity):
        """

        :param entity: The identity of the parent entity.
        :type entity: int

        :return:
        :rtype: Component
        """
        if not self.has_component(entity):
            raise Exception("Error: Component type {0} for entity id {1} does not exist."
                            .format(self._component_type, entity))
        return self._components[entity]

    def has_component(self, entity):
        """

        :param entity: The identity of the parent entity.
        :type entity: int

        :return:
        :rtype: bool
        """
        return entity in self._components

    @staticmethod
    def create():
        """
        Static Factory method.

        :return: A new component manager instance.
        :rtype: ComponentManager
        """
        return ComponentManager()
