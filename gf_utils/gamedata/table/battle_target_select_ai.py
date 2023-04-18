from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class BattleTargetSelectAiInstance:
    id: int  # 1
    description: str  # '对自身释放'
    target_type: int  # 4
    target_number: int  # 1
    target_priority: int  # 1
    select_order: str  # '0'
    is_ascend_order: str  # '0'
    is_ingore_range: int  # 1
    is_search_all: int  # 0
    list_ranking: int  # 1
    target_buff_id: int  # 0
    target_parameter: int  # 0
    buff_trigger_type: int  # 6
    is_buff_type: int  # 0


class BattleTargetSelectAi(ConfigTable):
    name = "battle_target_select_ai"

    def add_instance(self, k):
        return BattleTargetSelectAiInstance(**self._data[k])
