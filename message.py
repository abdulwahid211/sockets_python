class Message:
    def __init__(self, _name, _message):
        self._name = _name
        self._message = _message

    def updateMessage(self, m):
        self._message = m
