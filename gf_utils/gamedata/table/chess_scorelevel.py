from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class ChessScorelevelInstance:
    id: int  # 1
    name: str  # '士官'
    code: str  # '1'
    score_floor: int  # 0
    score_ceilling: int  # 24
    score_get: str  # '1:10,6,3,0;2:4,1'
    prize: int  # 0


class ChessScorelevel(ConfigTable):
    name = "chess_scorelevel"

    def add_instance(self, k):
        return ChessScorelevelInstance(**self._data[k])
