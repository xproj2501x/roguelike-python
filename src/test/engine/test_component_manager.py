import unittest

from src.roguelike.engine.component_manager import ComponentManager


class ComponentManagerTest(unittest.TestCase):
    """
    Test suite for ComponentManager class
    """
    def setUp(self):
        self._component_manager = ComponentManager()

    def test_create_component(self):
        """
        Test for ComponentManager.create_component method.
        """
        self._component_manager.create_component(1, 1, {'a': 1, 'b': 2})
        self.assertEquals(self._component_manager.has_component(1, 1), True)

    def test_create_component_exception(self):
        """
        Test for ComponentManager.create_component method.
        """
        self._component_manager.create_component(1, 1, {'a': 1, 'b': 2})
        with self.assertRaises(Exception) as component_manager:
            self._component_manager.create_component(1, 1, {'a': 1, 'b': 2})
            self.assertEquals(component_manager.exception,
                              "Error: Component type 1 is already attached to entity id 1.")

    def test_destroy_component(self):
        """
        Test for ComponentManager.destroy_component method.
        """
        self._component_manager.create_component(1, 1, {'a': 1, 'b': 2})
        self._component_manager.destroy_component(1, 1)
        self.assertEquals(self._component_manager.has_component(1, 1), False)

    def test_destroy_component_exception(self):
        """
        Test for ComponentManager.destroy_component method.
        """
        with self.assertRaises(Exception) as component_manager:
            self._component_manager.destroy_component(1, 1)
            self.assertEquals(component_manager.exception, "Error: Component type 1 is not attached to entity id 1")

    def test_update_component(self):
        """
        Test method for ComponentManager.update_component method.
        """
        self._component_manager.create_component(1, 1, {'a': 1, 'b': 2})
        self._component_manager.update_component(1, 1, {'a': 2, 'b': 3})

    def test_update_component_exception(self):
        """
        Test method for ComponentManager.update_component method.
        """
        with self.assertRaises(Exception) as component_manager:
            self._component_manager.update_component(1, 1)
            self.assertEquals(component_manager.exception, "Error: Component type 1 is not attached to entity id 1")

    def test_get_component(self):
        """
        Test method for ComponentManager.get_component method.
        """

    def test_get_component_exception(self):
        """
        Test method for ComponentManager.get_component method.
        """

    def test_has_component(self):
        pass
