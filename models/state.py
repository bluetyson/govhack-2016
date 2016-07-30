class State:
    def __init__(self, node):
        self.politician_id = node[0][0].find("name.id").text
        self.type = node.tag

    def key(self):
        return self.politician_id + "." + self.type
