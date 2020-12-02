import argparse
import os
from typing import Dict, List, Tuple

from argparse_types import ArgparseType
from database_connectors.iconnector import IConnector
from dotenv import load_dotenv
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
        self._load_env_variables()

        students_data, rooms_data = self._load_students_and_rooms_data_from_file()

        current_connector: IConnector = settings.available_database_connectors.get(
            settings.current_database_connector)(user=os.getenv("MYSQL_USER"),
                                                 password=os.getenv(
                                                     "MYSQL_PASSWORD"),
                                                 database=os.getenv(
                                                     "MYSQL_DATABASE")
                                                 )
        current_connector.connect()
        current_connector.insert_students_and_rooms_data(
            students_data, rooms_data)
        for name in settings.name_of_queries_to_database:
            sql_response = getattr(current_connector, name)()
            serialized_data = self._serialize_result_of_sql_queries(
                sql_response)
            self._write_to_file_serialized_data(name, serialized_data)
        current_connector.add_indexes_to_tables()
        current_connector.disconnect()

    def _load_env_variables(self):
        # load env variables .env file
        load_dotenv(override=True)

    def _load_students_and_rooms_data_from_file(self) -> Tuple[List[Dict]]:
        current_loader: IFileLoader = settings.available_loaders_from_file.get(
            settings.current_loader_format)()

        students_data = current_loader.read(self.students_path)
        rooms_data = current_loader.read(self.rooms_path)
        return students_data, rooms_data

    def _get_current_connector_to_database(self) -> IConnector:
        current_connector_class = settings.available_database_connectors.get(
            settings.current_database_connector)
        current_connector: IConnector = current_connector_class(
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )
        return current_connector

    def _serialize_result_of_sql_queries(self, sql_response: List[Dict]) -> str:
        current_serializer: ISerializer = settings.available_serializers.get(
            self.output_format)()
        serialized_data = current_serializer.serialize(sql_response)
        return serialized_data

    def _write_to_file_serialized_data(self, filename: str, serialized_data: str) -> None:
        text_writer: IFileWriter = settings.available_writers_to_file.get(
            "text")()
        text_writer.write(serialized_data, "result_folder/" +
                          filename, self.output_format)


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
