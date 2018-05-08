import unittest

from src.roguelike.engine.entity import Entity

IDENTITY = 1


class EntityTest(unittest.TestCase):
    """
    Test suite for Entity class.
    """

    def setUp(self):
        self._entity = Entity(IDENTITY)

    def test_identity(self):
        """
        Test for Entity.identity property.
        """
        self.assertEquals(self._entity.identity, IDENTITY)

    def test_attach_component(self):
        """
        Test for Entity.attach_component method
        """
        self._entity.attach_component(IDENTITY)
        self.assertEquals(self._entity.has_component(IDENTITY), True)

    def test_attach_component_duplicate_exception(self):
        """
        Test for Entity.attach_component method exception.
        """
        self._entity.attach_component(IDENTITY)
        with self.assertRaises(Exception) as entity:
            self._entity.attach_component(1)
            self.assertEquals(entity.exception, "Error: Component type 1 already attached to entity 1")

    def test_detach_component(self):
        """
        Test for Entity.detach_component method
        """
        self._entity.attach_component(IDENTITY)
        self._entity.detach_component(IDENTITY)
        self.assertEquals(self._entity.has_component(IDENTITY), False)

    def test_detach_component_not_attached_exception(self):
        """
        Test for Entity.attach_component method exception
        """
        with self.assertRaises(Exception) as entity:
            self._entity.attach_component(IDENTITY)
            self.assertEquals(entity.exception, "Error: Component type 1 not attached to entity entity 1")

    def test_has_component_true(self):
        """
        Test for Entity.has_component method returns True.
        """
        self._entity.attach_component(IDENTITY)
        result = self._entity.has_component(IDENTITY)
        self.assertEquals(result, True)

    def test_has_component_false(self):
        """
        Test for Entity.has_component method returns False.
        """
        result = self._entity.has_component(IDENTITY)
        self.assertEquals(result, False)

    def test_create(self):
        """
        Test for Entity.create static method.
        """
        entity = Entity.create(IDENTITY)
        self.assertEquals(type(entity), Entity)

    def test_create_identity_exception(self):
        """
        Test for Entity.create static method exception.
        """
        with self.assertRaises(Exception) as entity:
            Entity.create(None)
            self.assertEquals(entity.exception, "Error: Entity id cannot be None.")
