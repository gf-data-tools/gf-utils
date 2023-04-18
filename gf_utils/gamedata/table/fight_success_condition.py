from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class FightSuccessConditionInstance:
    id: int  # 1
    name: str  # '战斗胜利'
    type: int  # 1
    desc: str  # '关卡胜利'
    condition_coef: str  # '1'
    score_coef: int  # 100


class FightSuccessCondition(ConfigTable):
    name = "fight_success_condition"

    def add_instance(self, k):
        return FightSuccessConditionInstance(**self._data[k])
