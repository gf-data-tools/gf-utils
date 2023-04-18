from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class SkinClassInstance:
    id: int  # 1
    theme_type: int  # 7
    name: str  # '万圣狂欢'


class SkinClass(ConfigTable):
    name = "skin_class"

    def add_instance(self, k):
        return SkinClassInstance(**self._data[k])
