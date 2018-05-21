class MessageService:

    def __init__(self):
        self._subscriptions = {}

    def subscribe(self, subject, subscriber):
        """
        Adds a subscriber callback for the subject.
        :param subject:
        :type subject: str
        :param subscriber: The callback function for the subscription
        :type subscriber: func
        """
        if subject not in self._subscriptions:
            self._subscriptions[subject] = []
        self._subscriptions[subject].append(subscriber)

    def unsubscribe(self, subject, subscriber):
        """
        Removes a subscriber callback from the subject.
        :param subject:
        :type subject: str
        :param subscriber: The callback function for the subscription
        :type subscriber: func
        """
        if subject not in self._subscriptions:
            return
        subscribers = self._subscriptions[subject]
        if subscribers.count(subscriber) == 0:
            return
        index = subscribers.index(subscriber)
        del subscribers[index]

    def send(self, message):
        """
        Sends a message to all callbacks subscribed to the subject.
        :param message: The message to be sent.
        :type message: object
        """
        subscribers = self._subscriptions[message.subject] if self._subscriptions[message.subject] else []
        for subscriber in subscribers:
            subscriber.handle_message(message)

    @staticmethod
    def create():
        """
        Static factory method.

        :return: A new message service instance.
        :rtype: MessageService
        """
        return MessageService()
