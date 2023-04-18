from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class SangvisExpInstance:
    lv: int  # 1
    exp: int  # 100


class SangvisExp(ConfigTable):
    name = "sangvis_exp"

    def add_instance(self, k):
        return SangvisExpInstance(**self._data[k])
