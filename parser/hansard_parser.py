import xml.etree.ElementTree as ET

def parse_xml(xml):
    tree = ET.parse(xml)
    root = tree.getroot()
    print root.tag

if __name__=="__main__":
    parse_xml("sample.xml")
