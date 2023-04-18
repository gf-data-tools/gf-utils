from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class EnemyVoiceInfoInstance:
    id: str  # '1'
    code: str  # '_APPEAR1_'
    trigger_parameter: str  # '0'


class EnemyVoiceInfo(ConfigTable):
    name = "enemy_voice_info"

    def add_instance(self, k):
        return EnemyVoiceInfoInstance(**self._data[k])
