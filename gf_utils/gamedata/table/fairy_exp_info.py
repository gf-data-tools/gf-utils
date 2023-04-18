from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class FairyExpInfoInstance:
    id: str  # '1'
    exp: str  # '0'


class FairyExpInfo(ConfigTable):
    name = "fairy_exp_info"

    def add_instance(self, k):
        return FairyExpInfoInstance(**self._data[k])
