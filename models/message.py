class Message:
    def __init__(self, state, message):
        self.state = state
        thing = self.state.key.split(".")[1]
        self.type = thing
        self.content = message
