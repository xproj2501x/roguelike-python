from roguelike.engine import MAX_COMPONENTS, MAX_ENTITIES, CREATE_COMPONENT, DESTROY_COMPONENT
from roguelike.engine.component import Component


class ComponentManager:

    # def __init__(self, message_service):
    def __init__(self):
        # self._message_service = message_service
        self._components = [None] * MAX_COMPONENTS
        # self._message_service.subscribe(CREATE_COMPONENT, self)
        # self._message_service.subscribe(DESTROY_COMPONENT, self)

    def create_component(self, component_type, entity, state):
        """
        Creates a new instance of component of the specified type for the specified entity.

        :param component_type: The type of component be created.
        :type component_type: int
        :param entity: The identity of the parent entity.
        :type entity: int
        :param state:
        :type state: dict

        :raises: Exception if the component type is already attached to the entity.
        """
        if not self._components[component_type]:
            self._components[component_type] = [None] * MAX_ENTITIES
        if self.has_component(component_type, entity):
            raise Exception("Error: Component type {0} is already attached to entity id {1}."
                            .format(component_type, entity))
        component = Component.create(entity, state)
        self._components[component_type][entity] = component

    def destroy_component(self, component_type, entity):
        """
        Destroys a component of the specified type for the specified entity.

        :param component_type: The type of component be destroyed.
        :type component_type: str
        :param entity: The identity of the parent entity.
        :type entity: int
        """
        if not self.has_component(component_type, entity):
            raise Exception("Error: Component type {0} is not attached to entity id {1}".format(component_type, entity))
        self._components[component_type][entity] = None

    def update_component(self, component_type, entity, state):
        """
        Updates a component for the specified entity with the new state.

        :param component_type: The type of component be updated.
        :type component_type: str
        :param entity: The identity of the parent entity.
        :type entity: int
        :param state:
        :type state: dict
        """
        if not self.has_component(component_type, entity):
            raise Exception("Error: Component type {0} is not attached to entity id {1}".format(component_type, entity))
        component = self._components[component_type][entity]
        component.update(state)

    def get_component(self, component_type, entity):
        """

        :param component_type: The type of component.
        :type component_type: str
        :param entity: The identity of the parent entity.
        :type entity: int

        :return:
        :rtype: Component
        """
        if not self.has_component(entity):
            raise Exception("Error: Component type {0} for entity id {1} does not exist."
                            .format(self._component_type, entity))
        return self._components[component_type][entity]

    def has_component(self, component_type, entity):
        """

        :param component_type: The type of component.
        :type component_type: int
        :param entity: The identity of the parent entity.
        :type entity: int

        :return:
        :rtype: bool
        """
        if not self._components[component_type][entity]:
            return False
        return True

    # def handle_message(self, message):
    #     if message.subject == CREATE_COMPONENT:
    #         self.create_component(message.body.entity, message.body.component_type, message.body.state)
    #     if message.subject == DESTROY_COMPONENT:
    #         pass

    @staticmethod
    def create(message_service):
        """
        Static Factory method.

        :param message_service:
        :type message_service: MessageService

        :return: A new component manager instance.
        :rtype: ComponentManager
        """
        return ComponentManager(message_service)
