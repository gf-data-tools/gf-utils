from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class EquipCategoryInstance:
    category: int  # 0
    name: str  # '全部'
    en_name: str  # 'Show All'
    code: str  # ''


class EquipCategory(ConfigTable):
    name = "equip_category"

    def add_instance(self, k):
        return EquipCategoryInstance(**self._data[k])
