from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class BattleTriggerInstance:
    id: int  # 0
    type: int  # 1
    target: int  # 1
    parameter: str  # '0'
    buff_id: int  # 0
    is_buff_type: int  # 0


class BattleTrigger(ConfigTable):
    name = "battle_trigger"

    def add_instance(self, k):
        return BattleTriggerInstance(**self._data[k])
