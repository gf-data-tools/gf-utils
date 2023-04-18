from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class EnemyVoiceInfoInstance:
    id: str  # '1'
    code: str  # '_APPEAR1_'
    trigger_parameter: str  # '0'


class EnemyVoiceInfo(ConfigTable):
    name = "enemy_voice_info"

    def add_instance(self, k):
        return EnemyVoiceInfoInstance(**self._data[k])
