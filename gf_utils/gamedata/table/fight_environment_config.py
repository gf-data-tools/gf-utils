from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class FightEnvironmentConfigInstance:
    id: int  # 1
    transform_type: int  # 1
    transform_number: str  # '2'
    transform_result_add: str  # '701'
    transform_result_delete: str  # '1'


class FightEnvironmentConfig(ConfigTable):
    name = "fight_environment_config"

    def add_instance(self, k):
        return FightEnvironmentConfigInstance(**self._data[k])
