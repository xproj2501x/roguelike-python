class SystemManager:

    def __init__(self, message_service):
        self._message_service = message_service
        self._systems = []
        self._message_service.subscribe()

    def update(self, delta):
        """

        """
        for system in self._systems:
            system.update()

    def register(self, system):
        """

        :param system:
        :type system: System
        """


    @staticmethod
    def create(message_service):
        """
        Static factory method.

        :param message_service:
        :type message_service: MessageService

        :return: A new system manager instance.
        :rtype: SystemManager
        """
        return SystemManager(message_service)
