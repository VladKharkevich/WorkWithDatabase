from abc import ABCMeta, abstractmethod


class ISerializer(metaclass=ABCMeta):
    @abstractmethod
    def serialize(self, data) -> str:
        pass
