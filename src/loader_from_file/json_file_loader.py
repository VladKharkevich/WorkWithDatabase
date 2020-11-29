import json
from typing import Dict, List, Union

from .ifileloader import IFileLoader


class JSONFileLoader(IFileLoader):
    def read(self, path: str) -> Union[List, Dict]:
        with open(path, "r") as file:
            data = json.load(file)
        return data
