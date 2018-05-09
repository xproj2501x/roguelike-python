class SystemManager:

    def __init__(self):
        self._systems = []

    def update(self):
        """

        """
        for system in self._systems:
            system.update()

    @staticmethod
    def create():
        """
        Static factory method.

        :return: A new system manager instance.
        :rtype: SystemManager
        """
        return SystemManager()
