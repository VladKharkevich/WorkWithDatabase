import json

from .iserializer import ISerializer


class JSONSerializer(ISerializer):
    def serialize(self, data) -> str:
        return json.dumps(data, sort_keys=True, indent=4)
