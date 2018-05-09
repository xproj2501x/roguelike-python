from src.roguelike.engine import MAX_COMPONENTS


class Entity:

    @property
    def identity(self):
        """
        Read only property.

        :return: The identifier of the entity.
        :rtype: string
        """
        return self._identity

    def __init__(self, identity):
        """
        :param identity: The identifier for the entity.
        :type identity: int
        """
        self._identity = identity
        self._components = [None] * MAX_COMPONENTS

    def attach_component(self, component):
        """
        Attaches a component to the entity.
        :param component: The type of component to be attached.
        :type component: int
        """
        if self.has_component(component):
            raise Exception("Error: Component type {0} already attached to entity {1}."
                            .format(component, self._identity))
        self._components[component] = True

    def detach_component(self, component):
        """
        Detaches a component from the entity.
        :param component: The type of component
        :type component: int
        """
        if not self.has_component(component):
            raise Exception("Error: Component type {0} not attached to entity {1}."
                            .format(component, self._identity))
        self._components[component] = None

    def has_component(self, component):
        """

        :param component: The type of component
        :type component: int

        :return:
        :rtype: bool
        """
        return self._components[component] is not None

    @staticmethod
    def create(identity):
        """
        Static factory method
        :param identity: The id for the entity
        :type identity: int

        :return: A new entity instance
        :rtype: Entity
        """
        if not identity and identity != 0:
            raise Exception("Error: Entity id cannot be None.")
        return Entity(identity)
