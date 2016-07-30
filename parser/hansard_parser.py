from models.politician import *
from models.state import *
import xml.etree.ElementTree as ET

class HansardParser:
    __excluded_ids = ["10000"]

    def parse(self, path_to_xml):
        xml = ET.parse(path_to_xml).getroot()
        politicians = self.__get_politicians(xml)
        states = self.__get_states(xml)
        print [x.get_state_type() for x in states]

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
