from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class BattleMovementInfoInstance:
    id: str  # '100'
    target: str  # '2'
    offset: str  # '2,0,0'
    distance: str  # '2'
    duration: str  # '2'
    cd: str  # '2'
    is_character: str  # '1'
    easing_type: str  # '0'


class BattleMovementInfo(ConfigTable):
    name = "battle_movement_info"

    def add_instance(self, k):
        return BattleMovementInfoInstance(**self._data[str(k)])
