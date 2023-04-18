from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class BattleWatchTriggerInstance:
    id: int  # 1001
    description: str  # '老李增益监视1'
    buff_judge: int  # 1000004733
    hurt_from: str  # '0'
    available_gun_type: str  # '0'
    hurt_type: str  # '0'
    is_hurt_body: int  # 0
    hurt_formula_target: int  # 0
    hurt_judge: int  # 0
    watched_skill_type: int  # 0
    watched_skill_group_id: int  # 0


class BattleWatchTrigger(ConfigTable):
    name = "battle_watch_trigger"

    def add_instance(self, k):
        return BattleWatchTriggerInstance(**self._data[k])
