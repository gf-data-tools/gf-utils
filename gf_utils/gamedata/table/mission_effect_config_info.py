from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class MissionEffectConfigInfoInstance:
    id: str  # '1'
    name: str  # '地雷出现'
    code: str  # 'dilei_chuxian'
    description: str  # '地雷'
    priority: str  # '0'
    duration: str  # '1.00'
    delay: str  # '0.00'
    size: str  # '0.80'
    offset: str  # '0,0'
    sound: str  # 'bb_noel_nachujiguanqiang'
    spine: str  # '0'
    if_starting: str  # '0'
    relative_position: str  # '0'
    rotation_offset: str  # ''
    is_focus: str  # '0'
    use_ease: str  # '0'


class MissionEffectConfigInfo(ConfigTable):
    name = "mission_effect_config_info"

    def add_instance(self, k):
        return MissionEffectConfigInfoInstance(**self._data[k])
