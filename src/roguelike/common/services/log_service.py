class LogService:

    def __init__(self):
        self._logs = []

    def clear(self):
        self._logs = []

    def _write(self, level, message):
        """
        Writes a new message to the log.
        :param level:
        :type level: str
        :param message:
        """
        self._logs.append(message)

    @staticmethod
    def create():
        """
        Static factory method.
        :return: A new log service instance.
        :rtype: LogService
        """
        return LogService()
