from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class FairyTypeInfoInstance:
    id: str  # '1'
    name: str  # '增益类'


class FairyTypeInfo(ConfigTable):
    name = "fairy_type_info"

    def add_instance(self, k):
        return FairyTypeInfoInstance(**self._data[k])
