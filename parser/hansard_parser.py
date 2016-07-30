import xml.etree.ElementTree as ET
import sys
sys.path.insert(0, "..")
from models import politician
def parse_xml(xml):
    tree = ET.parse(xml)
    root = tree.getroot()
    print root.tag

if __name__=="__main__":
    print "test"
