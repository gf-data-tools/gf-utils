from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class KalinaFavorInfoInstance:
    level: str  # '1'
    min_favor: str  # '50'
    skin_id: str  # '0'


class KalinaFavorInfo(ConfigTable):
    name = "kalina_favor_info"

    def add_instance(self, k):
        return KalinaFavorInfoInstance(**self._data[k])
