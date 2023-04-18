from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class ExploreAreaInstance:
    id: int  # 1
    name: str  # '城市'
    background: str  # 'bridge,iron,city,park'


class ExploreArea(ConfigTable):
    name = "explore_area"

    def add_instance(self, k):
        return ExploreAreaInstance(**self._data[k])
