class State:
    def __init__(self, name):
        self.name = name

    def get_politician_id(self):
        return self.name.split(".")[0]
    
    def get_state_type(self):
        return self.name.split(".")[1]
