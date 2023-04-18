from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class TeamAiInstance:
    id: int  # 1
    force_id: int  # 1
    ai_type: int  # -1
    name: str  # '夜战'
    description: str  # '无法判断敌方行动轨迹。'
    pic: str  # 'ai_random'
    color: str  # 'ffffff'


class TeamAi(ConfigTable):
    name = "team_ai"

    def add_instance(self, k):
        return TeamAiInstance(**self._data[k])
