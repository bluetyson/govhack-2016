from models.politician import *
from models.state import *
from markov import markov_structure, markov_text
import xml.etree.ElementTree as ET
from collections import OrderedDict

class HansardParser:
    __excluded_ids = ["10000"]

    def parse(self, path_to_xml):
        xml = ET.parse(path_to_xml).getroot()
        state_to_corpus = self.get_state_to_corpus(xml)
        states = [x[0] for x in state_to_corpus]
        generated_states = markov_structure.markov_chain(states).walk(len(states), states[0])
        generated_output = markov_text.markov_text(self.aggregate_state_to_corpus(state_to_corpus))
        print generated_output

    def element_to_string(self, element):
        return ' '.join(ET.tostring(element, encoding="utf-8", method="text").split())

    def get_state_to_corpus(self, xml):
        result = []      
        for node in xml.findall(".//talk.start/.."):
            state = State(node)
            corpus = [self.element_to_string(x) for x in node.find("talk.text")]
            if state.politician_id not in self.__excluded_ids:
                result.append((state.key(), corpus))
        return result
    
    def aggregate_state_to_corpus(self, state_to_corpus):
        result = dict()
        for item in state_to_corpus:
            state, corpus = item
            if result.has_key(state):
                result[state].append(corpus)
            else:
                result[state] = [corpus]
        return result

if __name__=="__main__":
    parser = HansardParser()
    parser.parse("sample.xml")
