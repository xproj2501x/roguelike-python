import unittest
import mock

from src.roguelike.engine.entity_manager import EntityManager


class EntityManagerTest(unittest.TestCase):
    """
    Test suite for EntityManager class
    """

    def setUp(self):
        self._entity_manager = EntityManager()

    @mock.patch('src.roguelike.engine.entity_manager.Entity.create')
    def test_create_entity(self, mock_create):
        """
        Test for EntityManager.create_entity method.
        """
        mock_create.return_value = mock.Mock(identity=mock.Mock(return_value=1))
        entity_id = self._entity_manager.create_entity()
        result = self._entity_manager.has_entity(entity_id)
        self.assertEquals(entity_id, result)

    def test_create_entity_sequential_identifier(self):
        """
        Test for EntityManager.create_entity method.
        """
        entity_one = self._entity_manager.create_entity()
        entity_two = self._entity_manager.create_entity()
        self.assertEquals(entity_one + 1, entity_two)
