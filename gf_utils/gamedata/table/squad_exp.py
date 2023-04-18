from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class SquadExpInstance:
    lv: int  # 1
    exp: int  # 0
    precise: int  # 20


class SquadExp(ConfigTable):
    name = "squad_exp"

    def add_instance(self, k):
        return SquadExpInstance(**self._data[k])
