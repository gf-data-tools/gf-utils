from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class MedalInfoInstance:
    id: str  # '1'
    name: str  # '精英狮鹫作战勋章'
    order: str  # '93'
    evo_step: str  # '1'
    appearance_id: str  # '1'
    item_id: str  # '100'
    medal_obtain: str  # '授予在大型限时活动中完成所有战斗挑战的指挥官。'
    medal_color: str  # '#009bff'
    is_date: str  # '0'
    decorate_code: str  # ''
    if_elite_medal: str  # '1'


class MedalInfo(ConfigTable):
    name = "medal_info"

    def add_instance(self, k):
        return MedalInfoInstance(**self._data[k])
