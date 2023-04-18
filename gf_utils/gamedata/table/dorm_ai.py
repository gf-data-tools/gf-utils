from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class DormAiInstance:
    id: int  # 0
    actions: str  # '1,2,4,5,16,17'
    up_rate: str  # '150,50,50,50,2000,2000'
    min_time: str  # '5,5,5,5,300,300'
    time_weight: str  # '1,1,1,1,5,5'
    move_speed: float  # 0.0
    interact_point: str  # ''
    interact_point_offset: str  # ''


class DormAi(ConfigTable):
    name = "dorm_ai"

    def add_instance(self, k):
        return DormAiInstance(**self._data[k])
