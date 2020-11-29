from abc import ABCMeta, abstractmethod


class IFileWriter(metaclass=ABCMeta):
    @abstractmethod
    def write(self, data: str, path: str, format: str) -> None:
        pass
