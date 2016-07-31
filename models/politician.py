class Politician:   
    def __init__(self, hansard_node):
        talker = hansard_node.find("talk.start").find("talker")
        self.id = talker.find("name.id").text
        self.name = talker.find("name").text
        self.party = talker.find("party").text
