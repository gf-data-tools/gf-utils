from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class Live2dMotionsInstance:
    id: int  # 306
    type: int  # 101
    motion_name: str  # 'motions/idle.mtn'
    touch_area: str  # '0'
    hold_time: str  # '0'
    probability: float  # 1.0
    voice: str  # ''
    text: str  # ''
    expression: str  # ''
    face_motion: str  # ''
    name: str  # 'live2d_motions-10000306'
    camera: int  # 0
    is_hurt: int  # 0
    level: int  # 0
    is_interrupt: int  # 0
    delay: int  # 0
    next_motions: str  # ''
    voice_code: str  # ''


class Live2dMotions(ConfigTable):
    name = "live2d_motions"

    def add_instance(self, k):
        return Live2dMotionsInstance(**self._data[k])
