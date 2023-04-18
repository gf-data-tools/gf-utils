from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class ChessMapInstance:
    id: int  # 1
    name: str  # '边陲之地'
    code: str  # 'FlightChessDesert_1'
    default_unlock: int  # 1
    unlock_item_id: int  # 0


class ChessMap(ConfigTable):
    name = "chess_map"

    def add_instance(self, k):
        return ChessMapInstance(**self._data[k])
