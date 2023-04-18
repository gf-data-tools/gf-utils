from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class MedalInstance:
    id: int  # 1
    name: str  # '精英狮鹫作战勋章'
    order: int  # 93
    evo_step: str  # '1'
    appearance_id: str  # '1'
    item_id: int  # 100
    medal_obtain: str  # '授予在大型限时活动中完成所有战斗挑战的指挥官。'
    medal_color: str  # '#009bff'
    is_date: int  # 0
    decorate_code: str  # ''


class Medal(ConfigTable):
    name = "medal"

    def add_instance(self, k):
        return MedalInstance(**self._data[k])
