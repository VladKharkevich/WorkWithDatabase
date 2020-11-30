from abc import ABCMeta, abstractmethod
from typing import List, Dict


class ISerializer(metaclass=ABCMeta):
    @abstractmethod
    def serialize(self, data: List[Dict]) -> str:
        pass
