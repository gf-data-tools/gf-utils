from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class MissionMappedInstance:
    id: int  # 31001
    mapped_missions: str  # '10196,10254'


class MissionMapped(ConfigTable):
    name = "mission_mapped"

    def add_instance(self, k):
        return MissionMappedInstance(**self._data[k])
