from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class GameConfigInfoInstance:
    parameter_name: str  # '2022_bikini_max_votes'
    parameter_type: str  # 'int'
    parameter_value: str  # '50'
    client_require: str  # '1'


class GameConfigInfo(ConfigTable):
    name = "game_config_info"

    def add_instance(self, k):
        return GameConfigInfoInstance(**self._data[k])
