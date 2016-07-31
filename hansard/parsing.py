from models.politician import *
from models.state import *
from models.hansard_node import *
from markov import markov_structure, markov_text
import xml.etree.ElementTree as ET
from collections import OrderedDict

class HansardParser:
    __excluded_ids = ["10000"]

    def parse(self, path_to_xml):
        xml = ET.parse(path_to_xml).getroot()
        hansard_nodes = self.get_hansard_nodes(xml)
        state_to_corpus = [x.get_state_and_corpus() for x in hansard_nodes]
        states = [x[0] for x in state_to_corpus]
        states_strings = [x.key for x in states]
        generated_states = markov_structure.markov_chain(states_strings).walk(len(states_strings), states[0])
        generated_output = markov_text.markov_text(self.aggregate_state_to_corpus(state_to_corpus))

        for state in generated_states:
            model = generated_output[state]
            message = Message(state, model.make_sentence())
            if message.content is not None:
                yield message

    def get_hansard_nodes(self, xml):
        return [HansardNode(x) for x in xml.findall(".//talk.start/..")]
    
    def aggregate_state_to_corpus(self, state_to_corpus):
        result = dict()
        for item in state_to_corpus:
            state, corpus = item
            if result.has_key(state):
                result[state] += corpus
            else:
                result[state] = corpus
        return result

if __name__=="__main__":
    parser = HansardParser()
    parser.parse("sample.xml")
