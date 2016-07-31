from models.politician import *

class State:
    def __init__(self, hansard_node):
        self.politician_id = Politician(hansard_node).id
        self.key = self.politician_id + "." + hansard_node.tag
