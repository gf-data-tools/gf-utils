from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class FairyTypeInstance:
    id: int  # 1
    name: str  # '增益类'
    en_name: str  # 'Support'


class FairyType(ConfigTable):
    name = "fairy_type"

    def add_instance(self, k):
        return FairyTypeInstance(**self._data[k])
