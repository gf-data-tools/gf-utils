from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class ChessSpotInstance:
    id: int  # 67
    chess_mission_id: int  # 1
    type: int  # 4
    neighbor: str  # '-5,9;-6,8'
    player_order: int  # 2
    next_jump_airport_point: str  # ''
    next_jump_airport_direction: int  # 0
    axial_coordinator_q: int  # -6
    axial_coordinator_r: int  # 9
    positive_direction: str  # '-6,8'
    negative_direction: str  # '-5,9'
    random_get: int  # 0
    grow_enemy_pool: str  # ''
    grow_enemy_pool_turn: str  # ''


class ChessSpot(ConfigTable):
    name = "chess_spot"

    def add_instance(self, k):
        return ChessSpotInstance(**self._data[k])
