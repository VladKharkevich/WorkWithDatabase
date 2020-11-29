import argparse
from typing import Dict, List

from argparse_types import ArgparseType
from loader_from_file.ifileloader import IFileLoader
from serializers.iserializer import ISerializer
from settings import settings
from writers_to_file.ifilewriter import IFileWriter


class App:
    def __init__(self, argv):
        self.students_path = argv.students
        self.rooms_path = argv.rooms
        self.output_format = argv.format

    def run(self):
        current_loader: IFileLoader = settings.available_loaders_from_file.get(
            settings.current_loader_format)()

        students_data = current_loader.read(self.students_path)
        rooms_data = current_loader.read(self.rooms_path)
        merge_rooms = self._merge_rooms_and_students(students_data, rooms_data)

        current_serializer: ISerializer = settings.available_serializers.get(
            self.output_format)()
        serialized_data = current_serializer.serialize(merge_rooms)
        text_writer: IFileWriter = settings.available_writers_to_file.get(
            "text")()
        text_writer.write(serialized_data, "result", self.output_format)

    def _merge_rooms_and_students(self, students: List[Dict], rooms: List[Dict]) -> List[Dict]:
        for room in rooms:
            room["students"] = []
        for student in students:
            room_id: int = student.get("room")
            room: Dict = rooms[room_id]
            room["students"].append(student.get("id"))
        return rooms


if __name__ == "__main__":
    # init argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "students", help="Path to json file with students", type=ArgparseType.students_filename)
    parser.add_argument("rooms", help="Path to json file with rooms",
                        type=ArgparseType.rooms_filename)
    parser.add_argument("format", help="Format of output file",
                        type=ArgparseType.file_format)
    args = parser.parse_args()

    App(args).run()
