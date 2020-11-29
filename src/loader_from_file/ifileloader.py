from abc import ABCMeta, abstractmethod

from typing import Dict, List, Union


class IFileLoader(metaclass=ABCMeta):
    @abstractmethod
    def read(self, path: str) -> Union[List, Dict]:
        pass
