class Politician:   
    def __init__(self, node):
        self.id = node.find("name.id").text
        self.name = node.find("name").text
