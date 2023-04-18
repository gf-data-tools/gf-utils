from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class ChessRandomSpotInstance:
    id: int  # 1
    spot_effect: str  # '503'


class ChessRandomSpot(ConfigTable):
    name = "chess_random_spot"

    def add_instance(self, k):
        return ChessRandomSpotInstance(**self._data[k])
