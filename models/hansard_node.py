from models.politician import *
from models.state import *
import xml.etree.ElementTree as ET


class HansardNode:
    def __init__(self, node):
        self.node = node
        self.state = State(node)
        self.politician = Politician(node)

    def get_corpus(self):
       	return [self.element_to_string(x) for x in self.node.find("talk.text")]

    def element_to_string(self, element):
        return ' '.join(ET.tostring(element, encoding="utf-8", method="text").split())

    def get_state_and_corpus(self):
        return (self.state, self.get_corpus())

    