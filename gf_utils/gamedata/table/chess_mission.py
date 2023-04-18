from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class ChessMissionInstance:
    id: int  # 1
    name: str  # '环形公路'
    chess_spotids: str  # '87,88,91,92,93,94,95,96,97,98,99,100,101,104,105,106,107,108,109,110,111,112,113,114,117,118,119,120,121,122,123,124,125,67,68,71,72,79,80,81,82,83,84,85,70,89,90,102,103,115,116,69'
    rotation: float  # 90.0
    camera_height_range: str  # '-7,-13'
    camera_angle_h: float  # -55.0
    camera_angle_l: float  # -60.0
    random_enemy_pool: str  # ''
    map_limit: str  # '-15,15,12,-12'
    map_id: str  # '1,4'
    global_limit: str  # '24.3,18'
    global_pos: str  # '-1.72,-24,-18'
    mission_icon: str  # 'FlightChess_ring'


class ChessMission(ConfigTable):
    name = "chess_mission"

    def add_instance(self, k):
        return ChessMissionInstance(**self._data[k])
