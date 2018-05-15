from src.roguelike.engine import MAX_ENTITIES
from src.roguelike.engine.entity import Entity
from src.roguelike.engine.exceptions import EntityLimitExceeded


class EntityManager:

    def __init__(self):
        """

        """
        self._nextIdentity = -1
        self._entities = [None] * MAX_ENTITIES

    def create_entity(self):
        """
        Creates a new instance of Entity.

        :return: The identity for the new Entity.
        :rtype: int
        """
        self._nextIdentity += 1
        if self._nextIdentity >= MAX_ENTITIES:
            raise EntityLimitExceeded("Error: Entity limit {0} exceeded".format(MAX_ENTITIES))
        entity = Entity.create(self._nextIdentity)
        self._entities[self._nextIdentity] = entity
        return entity.identity

    def destroy_entity(self, identity):
        """
        Removes an entity from the simulation.
        :param identity: The identity of the entity.
        :type identity: int
        """
        if not self.has_entity(identity):
            raise Exception("Error: Entity id {0} does not exit".format(identity))
        self._entities[identity] = None

    def has_entity(self, identity):
        """

        :param identity: The identity of the entity.
        :type identity: int

        :return:
        :rtype: bool
        """
        return self._entities[identity] is not None

    def get_entity(self, identity):
        """

        :param identity: The identity of the entity.
        :type identity: int

        :return:
        :rtype: Entity
        """
        if not self.has_entity(identity):
            raise Exception("Error: Entity id {0} does not exit".format(identity))
        return self._entities[identity]

    def attach_component_to_entity(self, identity, component):
        """

        :param identity: The identity of the entity.
        :type identity: int
        :param component: The type of component to attach.
        :type component: int

        """
        entity = self.get_entity(identity)
        entity.attach_component(component)

    def detach_component_from_entity(self, identity, component_type):
        """

        :param identity:
        :type identity: int
        :param component_type:
        :type component_type: int
        """
        entity = self.get_entity(identity)
        entity.detach_component(component_type)

    @staticmethod
    def create():
        """
        Static factory method
        :return: A new entity manager instance.
        :rtype: EntityManager
        """
        return EntityManager()
