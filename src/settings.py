from dataclasses import dataclass, field
from typing import Dict, List

from database_connectors.iconnector import IConnector
from database_connectors.mysql_connector import MySQLConnector
from loader_from_file.ifileloader import IFileLoader
from loader_from_file.json_file_loader import JSONFileLoader
from serializers.iserializer import ISerializer
from serializers.json_serializer import JSONSerializer
from serializers.xml_serializer import XMLSerializer
from writers_to_file.ifilewriter import IFileWriter
from writers_to_file.text_file_writer import TextFileWriter


@dataclass
class Settings():
    available_serializers: Dict[str, ISerializer] = field(default_factory=dict)
    available_loaders_from_file: Dict[str,
                                      IFileLoader] = field(default_factory=dict)
    available_writers_to_file: Dict[str,
                                    IFileWriter] = field(default_factory=dict)
    available_database_connectors: Dict[str,
                                        IConnector] = field(default_factory=dict)
    current_loader_format: str = ""
    current_database_connector: str = ""

    # name of methods which makes queries and name of result file
    name_of_queries_to_database: List[str] = field(default_factory=list)


settings = Settings()
settings.available_serializers['json'] = JSONSerializer
settings.available_serializers['xml'] = XMLSerializer

settings.available_loaders_from_file['json'] = JSONFileLoader
settings.current_loader_format = 'json'

settings.available_writers_to_file['text'] = TextFileWriter

settings.available_database_connectors['mysql'] = MySQLConnector
settings.current_database_connector = 'mysql'

settings.name_of_queries_to_database = ['select_list_room_with_count_of_students',
                                        'select_top_5_rooms_with_the_smallest_average_age',
                                        'select_top_5_rooms_with_the_biggest_age_difference',
                                        'select_list_room_with_different_sex_of_students'
                                        ]
