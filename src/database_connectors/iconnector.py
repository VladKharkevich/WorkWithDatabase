from abc import ABCMeta, abstractmethod
from typing import List, Dict


class IConnector(metaclass=ABCMeta):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def insert_students_and_rooms_data(self, students_data: List[Dict], rooms_data: List[Dict]) -> None:
        pass

    @abstractmethod
    def select_list_room_with_count_of_students(self) -> List[Dict]:
        pass

    @abstractmethod
    def select_top_5_rooms_with_the_smallest_average_age(self) -> List[Dict]:
        pass

    @abstractmethod
    def select_top_5_rooms_with_the_biggest_age_difference(self) -> List[Dict]:
        pass

    @abstractmethod
    def select_list_room_with_different_sex_of_students(self) -> List[Dict]:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass
