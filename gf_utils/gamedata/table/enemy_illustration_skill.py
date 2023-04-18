from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class EnemyIllustrationSkillInstance:
    id: int  # 1
    name: str  # '普通射击'
    description: str  # '攻击距离自己最近的我方单位'


class EnemyIllustrationSkill(ConfigTable):
    name = "enemy_illustration_skill"

    def add_instance(self, k):
        return EnemyIllustrationSkillInstance(**self._data[k])
