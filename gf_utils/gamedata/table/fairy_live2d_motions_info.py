from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class FairyLive2dMotionsInfoInstance:
    id: str  # '101'
    type: str  # '1'
    motion_name: str  # 'motions/daiji_idle.mtn'
    touch_area: str  # '0'
    hold_time: str  # '0'
    probability: str  # '1.00'
    voice: str  # ''
    text: str  # ''
    expression: str  # ''
    face_motion: str  # ''
    name: str  # 'fairy_live2d_motions-10000101'
    camera: str  # '0'


class FairyLive2dMotionsInfo(ConfigTable):
    name = "fairy_live2d_motions_info"

    def add_instance(self, k):
        return FairyLive2dMotionsInfoInstance(**self._data[k])
