from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class SquadColorInstance:
    id: int  # 1
    rgb: str  # '239,107,67'
    fliter_text: str  # '橙,Orange'
    fliter_pic: str  # 'red'
    rank_weight: str  # '100,100'


class SquadColor(ConfigTable):
    name = "squad_color"

    def add_instance(self, k):
        return SquadColorInstance(**self._data[k])
