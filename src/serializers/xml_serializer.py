from xml.dom import minidom
from xml.etree import ElementTree

from .iserializer import ISerializer

# xml.etree is not external library!
# https://docs.python.org/3/library/xml.etree.elementtree.html


class XMLSerializer(ISerializer):
    def serialize(self, data) -> str:
        root = ElementTree.Element("rooms")
        for merge_room in data:
            room_node = ElementTree.SubElement(root, "room")
            ElementTree.SubElement(room_node, "id").text = str(
                merge_room.get("id"))
            ElementTree.SubElement(
                room_node, "name").text = merge_room.get("name")
            students_node = ElementTree.SubElement(room_node, "students")
            for student in merge_room.get("students"):
                ElementTree.SubElement(
                    students_node, "student").text = str(student)
        tree = ElementTree.ElementTree(root)
        return minidom.parseString(ElementTree.tostring(root)).toprettyxml(indent="   ")
