from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class ChessChoiceStageInstance:
    id: int  # 1
    name: str  # '定向部署'
    type: int  # 1
    parameter: str  # '60301'
    init_time: str  # '1,2'
    cd: int  # 3
    code: str  # 'AirdropIcon_1'
    description: str  # '获得1个部署道具卡<color=#ffb400ff>运兵站</color>'
    probability: int  # 10000


class ChessChoiceStage(ConfigTable):
    name = "chess_choice_stage"

    def add_instance(self, k):
        return ChessChoiceStageInstance(**self._data[k])
