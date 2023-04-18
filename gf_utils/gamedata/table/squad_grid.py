from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class SquadGridInstance:
    id: int  # 1
    grid: str  # '1,1'
    grid_number: int  # 1
    rank_weight: str  # '100,100'
    code: str  # 'grid1'


class SquadGrid(ConfigTable):
    name = "squad_grid"

    def add_instance(self, k):
        return SquadGridInstance(**self._data[k])
