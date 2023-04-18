from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class ChessGashaRewardInstance:
    id: int  # 1
    item_ids: str  # ''
    gift: str  # '573-1'
    prize_id: int  # 0
    type: int  # 1
    tickets_num: int  # 3000


class ChessGashaReward(ConfigTable):
    name = "chess_gasha_reward"

    def add_instance(self, k):
        return ChessGashaRewardInstance(**self._data[k])
