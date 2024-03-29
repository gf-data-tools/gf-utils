from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class SangvisCharacterTypeInstance:
    id: int  # 0
    name: str  # '全体'
    description: str  # '全体'


class SangvisCharacterType(ConfigTable):
    name = "sangvis_character_type"

    def add_instance(self, k):
        return SangvisCharacterTypeInstance(**self._data[k])
