from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class ExtraSpineInstance:
    id: int  # 2101
    name: str  # '田园猫（黄）'
    spine_code: str  # 'pet_cat4'
    scale: int  # 68
    ai: int  # 2100
    explore_tag: str  # '1001'


class ExtraSpine(ConfigTable):
    name = "extra_spine"

    def add_instance(self, k):
        return ExtraSpineInstance(**self._data[k])
