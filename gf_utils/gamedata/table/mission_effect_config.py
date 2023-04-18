from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class MissionEffectConfigInstance:
    id: int  # 1
    name: str  # '地雷出现'
    code: str  # 'dilei_chuxian'
    description: str  # '地雷'
    priority: int  # 0
    duration: float  # 1.0
    delay: float  # 0.0
    size: float  # 0.8
    sound: str  # 'bb_noel_nachujiguanqiang'
    spine: int  # 0
    if_starting: int  # 0
    relative_position: str  # '0'
    offset: str  # '0,0'
    rotation_offset: str  # ''
    is_focus: int  # 0
    use_ease: int  # 0


class MissionEffectConfig(ConfigTable):
    name = "mission_effect_config"

    def add_instance(self, k):
        return MissionEffectConfigInstance(**self._data[k])
