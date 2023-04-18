from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class ChessBuffInstance:
    id: int  # 101
    name: str  # '行动力提升'
    code: str  # 'FlightChessBuff_3'
    description: str  # '行动力+1'
    max_tier: int  # 99
    type: int  # 102
    duration_type: int  # 1
    duration: int  # 1
    parameter: str  # '1'
    trigger_creation_id: int  # 0
    creation_id: int  # 8
    available_gun_type: str  # '0'
    ui_control: int  # 0


class ChessBuff(ConfigTable):
    name = "chess_buff"

    def add_instance(self, k):
        return ChessBuffInstance(**self._data[k])
