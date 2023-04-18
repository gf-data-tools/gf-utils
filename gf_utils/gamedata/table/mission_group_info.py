from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class MissionGroupInfoInstance:
    id: str  # '1'
    reset_missions: str  # '10051,10052,10053,10054,10055,10056,10057,10058,10059,10060,10061,10062,10063,10064'
    reset_draw_events: str  # '1'
    reset_mission_keys: str  # '1'
    campaign: str  # '-16'
    difficulty: str  # '0'


class MissionGroupInfo(ConfigTable):
    name = "mission_group_info"

    def add_instance(self, k):
        return MissionGroupInfoInstance(**self._data[k])
