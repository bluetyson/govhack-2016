from models import politician
import xml.etree.ElementTree as ET

class HansardParser:

    def parse(self, path_to_xml):
        xml = ET.parse(path_to_xml).getroot()
        politicians = self.__get_politicians_from_xml(xml)
        print list(politicians)
        

    def __get_politicians_from_xml(self, xml):
        for node in xml.findall(".//talker"):
            yield Politician(node)
        


if __name__=="__main__":
    parser = HansardParser()
    parser.parse("sample.xml")
