from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class MissionKeyInfoInstance:
    id: str  # '1'
    item_id: str  # '0'


class MissionKeyInfo(ConfigTable):
    name = "mission_key_info"

    def add_instance(self, k):
        return MissionKeyInfoInstance(**self._data[k])
