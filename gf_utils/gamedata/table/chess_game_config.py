from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class ChessGameConfigInstance:
    id: int  # 1
    parameter_name: str  # 'crew_mode'
    parameter_type: str  # 'string'
    parameter_value: str  # '1,2'


class ChessGameConfig(ConfigTable):
    name = "chess_game_config"

    def add_instance(self, k):
        return ChessGameConfigInstance(**self._data[k])
