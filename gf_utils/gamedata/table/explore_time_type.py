from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class ExploreTimeTypeInstance:
    id: int  # 1
    duration: int  # 7200
    reward_item_type: str  # '1,3'
    mp: int  # 300
    ammo: int  # 300
    mre: int  # 300
    part: int  # 100
    draw_event_id: int  # 0


class ExploreTimeType(ConfigTable):
    name = "explore_time_type"

    def add_instance(self, k):
        return ExploreTimeTypeInstance(**self._data[k])
