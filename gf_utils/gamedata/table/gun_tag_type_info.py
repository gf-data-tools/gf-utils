from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class GunTagTypeInfoInstance:
    id: str  # '0'
    type_name: str  # '全部'
    en_name: str  # 'All'


class GunTagTypeInfo(ConfigTable):
    name = "gun_tag_type_info"

    def add_instance(self, k):
        return GunTagTypeInfoInstance(**self._data[k])
