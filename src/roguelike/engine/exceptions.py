class EngineException(Exception):

    def __init__(self, message, data):
        super(EngineException, self).__init__(message)


class EntityLimitExceeded(EngineException):
    pass
