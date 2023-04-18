from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class ChessSelectframeInstance:
    id: int  # 1
    select_num: int  # 2
    itemlanguage_id: str  # '280125,280057'
    code: str  # 'selection_1,selection_2'
    des: str  # '恭喜，您掷出了<color=#ffb400ff>6点</color>\n可以选择<color=#ffb400ff>移动一枚已上阵棋子</color>前进，也可以选择<color=#ffb400ff>部署一枚新的棋子</color>。\n同时，您将获取一次<color=ffb400ff>额外的行动投掷机会</color>！（每回合最多获得二次额外的行动投掷机会）'
    preview: str  # 'AttentionGroup,ChessOnboard'


class ChessSelectframe(ConfigTable):
    name = "chess_selectframe"

    def add_instance(self, k):
        return ChessSelectframeInstance(**self._data[k])
