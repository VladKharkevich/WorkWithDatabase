import json
from typing import List, Dict

from .iserializer import ISerializer


class JSONSerializer(ISerializer):
    def serialize(self, data: List[Dict]) -> str:
        return json.dumps(data, sort_keys=True, indent=4, default=str)
