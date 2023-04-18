from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class FairyTalentInstance:
    id: int  # 755192
    rank: int  # 0
    type_id: int  # 1
    name: str  # '布局型'


class FairyTalent(ConfigTable):
    name = "fairy_talent"

    def add_instance(self, k):
        return FairyTalentInstance(**self._data[k])
