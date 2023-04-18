from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class SangvisExpInstance:
    lv: int  # 1
    exp: int  # 100


class SangvisExp(ConfigTable):
    name = "sangvis_exp"

    def add_instance(self, k):
        return SangvisExpInstance(**self._data[k])
