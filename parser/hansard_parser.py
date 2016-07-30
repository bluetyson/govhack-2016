from models.politician import *
from models.state import *
from markov import markov_structure
import xml.etree.ElementTree as ET

class HansardParser:
    __excluded_ids = ["10000"]

    __take = 20

    def parse(self, path_to_xml):
        xml = ET.parse(path_to_xml).getroot()
        politicians = self.__get_politicians(xml)

        print '##Corpus'
        states = list(self.__get_states(xml))
        print [x.name for x in states[:self.__take]]
        
        print '\n##Output'
        model = markov_structure.markov_chain(states)
        print [x.name for x in model.walk(self.__take)]

    def __get_politicians(self, xml):
        for node in xml.findall(".//talker"):
            yield Politician(node)

    def __get_states(self, xml):
        for node in xml.findall(".//talk.start/.."):
            id = node[0][0].find("name.id").text
            if id not in self.__excluded_ids:
                yield State(id + "." + node.tag)

if __name__=="__main__":
    parser = HansardParser()
    parser.parse("sample.xml")
