from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class FightEnvironmentSkillInstance:
    id: int  # 1
    name: str  # '能量护盾'
    desc: str  # '战斗中为本梯队内的所有冲锋枪张开护盾,每个护盾最多吸收40点伤害。'
    if_display: int  # 1
    code: str  # 'shield'
    skill_group: str  # '900101'


class FightEnvironmentSkill(ConfigTable):
    name = "fight_environment_skill"

    def add_instance(self, k):
        return FightEnvironmentSkillInstance(**self._data[k])
