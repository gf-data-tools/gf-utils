from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class TheaterSelectionInstance:
    id: int  # 101
    name: str  # '灰烬山丘'
    description: str  # 'theater_selection-20000101'
    scout_material_number: str  # '10'
    scout_material: int  # 47
    scout_pt: int  # 30


class TheaterSelection(ConfigTable):
    name = "theater_selection"

    def add_instance(self, k):
        return TheaterSelectionInstance(**self._data[k])
