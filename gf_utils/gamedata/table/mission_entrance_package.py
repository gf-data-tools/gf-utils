from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class MissionEntrancePackageInstance:
    id: int  # 1051000
    value: str  # '10510,10510;10950,10950'


class MissionEntrancePackage(ConfigTable):
    name = "mission_entrance_package"

    def add_instance(self, k):
        return MissionEntrancePackageInstance(**self._data[k])
