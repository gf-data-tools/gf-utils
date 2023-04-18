from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class ExploreDestinationInstance:
    id: int  # 1
    area_id: int  # 1
    background: str  # ''


class ExploreDestination(ConfigTable):
    name = "explore_destination"

    def add_instance(self, k):
        return ExploreDestinationInstance(**self._data[k])
