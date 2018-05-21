import unittest

from src.roguelike.engine.entity_manager import EntityManager


class EntityManagerTest(unittest.TestCase):
    """
    Test suite for EntityManager class
    """

    def setUp(self):
        self._entity_manager = EntityManager()

    def test_create_entity(self):
        """
        Test for EntityManager.create_entity method.
        """
        entity_id = self._entity_manager.create_entity()
        result = self._entity_manager.has_entity(entity_id)
        self.assertEquals(result, True)

    def test_create_entity_sequential_identifier(self):
        """
        Test for EntityManager.create_entity method.
        """
        entity_one = self._entity_manager.create_entity()
        entity_two = self._entity_manager.create_entity()
        self.assertEquals(entity_one + 1, entity_two)

    def test_create_entity_max_exception(self):
        for x in range(1, 255):
            self._entity_manager.create_entity()
        with self.assertRaises(Exception) as entity_manager:
            self._entity_manager.create_entity()
            self.assertEquals(entity_manager.exception, "Error: Entity limit 255 exceeded")

    def test_destroy_entity(self):
        pass

    def test_destroy_entity_exception(self):
        pass

    def test_has_entity_true(self):
        pass

    def test_has_entity_false(self):
        pass
