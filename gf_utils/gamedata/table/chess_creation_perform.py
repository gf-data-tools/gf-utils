from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class ChessCreationPerformInstance:
    id: int  # 1
    code: str  # '手榴弹'
    start_type: int  # 2
    start_offset: str  # '0'
    destination_type: int  # 1
    destination_offset: str  # '0'
    route_type: int  # 2
    route_hight: int  # 1000
    speed: int  # 1500
    easing_type: int  # 0
    spin_velocity: int  # 3000
    rotate: str  # '0'
    duration: str  # '30'
    perform_duration: int  # 0
    is_tracing: int  # 0
    scale: str  # '2,2,2'
    is_hide: int  # 0
    trigger_creation: str  # '2,3'
    trigger_creation_delay: str  # '-1,-1'
    creation_type: int  # 0
    sound_order: str  # ''
    sound_delay: str  # ''
    creation_direction: int  # 0


class ChessCreationPerform(ConfigTable):
    name = "chess_creation_perform"

    def add_instance(self, k):
        return ChessCreationPerformInstance(**self._data[k])
