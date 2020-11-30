from typing import Dict, List
from xml.dom import minidom
from xml.etree import ElementTree

from .iserializer import ISerializer


class XMLSerializer(ISerializer):
    def serialize(self, data: List[Dict]) -> str:
        root = ElementTree.Element("result")
        for record in data:
            record_node = ElementTree.SubElement(root, "record")
            for key, value in record.items():
                ElementTree.SubElement(record_node, key).text = str(value)
        return minidom.parseString(ElementTree.tostring(root)).toprettyxml(indent="   ")
