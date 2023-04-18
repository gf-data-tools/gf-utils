from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class ChessRandomEnemyInstance:
    id: int  # 1
    enemy_id: str  # '1,2'
    random_spot_id: str  # '94,81,107,120'
    launch_time_type: int  # 1
    time: int  # 1


class ChessRandomEnemy(ConfigTable):
    name = "chess_random_enemy"

    def add_instance(self, k):
        return ChessRandomEnemyInstance(**self._data[k])
