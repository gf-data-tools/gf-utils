from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class SpotInstance:
    id: int  # 1
    mission_id: int  # 1
    type: int  # 1
    special_eft: int  # 0
    route: str  # '2'
    coordinator_x: int  # -806
    coordinator_y: int  # -1487
    enemy_team_id: int  # 0
    ally_team_id: int  # 0
    belong: int  # 1
    random_get: str  # '0'
    map_type: int  # 2
    curve_control: str  # '-700,-1567'
    active_cycle: str  # ''
    durability: str  # '0'
    map_route: str  # '2'
    map_code: str  # 'road'
    hostage_info: str  # ''
    building_id: int  # 0
    forbid_specialspot: str  # ''
    map_num: int  # 0
    package: int  # 0
    auto_teleport: str  # ''
    spot_effect: str  # ''


class Spot(ConfigTable):
    name = "spot"

    def add_instance(self, k):
        return SpotInstance(**self._data[k])
