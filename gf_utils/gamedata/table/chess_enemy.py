from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class ChessEnemyInstance:
    id: int  # 1
    code: str  # 'Weaver'
    name: str  # '衔尾蛇'
    power: int  # 12
    range: int  # 4
    hp: int  # 20
    ap: int  # 2
    attack_times: int  # 1
    armor: int  # 0
    armor_piercing: int  # 0
    reward_chip_ids: str  # '146:1,149:1,154:1'
    chip: str  # ''
    spine_direction: int  # 1
    attack_angle: int  # 120
    lifebar_offset: str  # '172,90'


class ChessEnemy(ConfigTable):
    name = "chess_enemy"

    def add_instance(self, k):
        return ChessEnemyInstance(**self._data[k])
