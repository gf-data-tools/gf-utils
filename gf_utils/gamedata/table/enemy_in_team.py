from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class EnemyInTeamInstance:
    id: int  # 1
    enemy_team_id: int  # 1
    enemy_character_type_id: int  # 90001
    coordinator_x: int  # 14
    coordinator_y: int  # 4
    level: int  # 1
    number: int  # 1
    is_advance: int  # 0
    def_percent: int  # 0
    batch: int  # 0


class EnemyInTeam(ConfigTable):
    name = "enemy_in_team"

    def add_instance(self, k):
        return EnemyInTeamInstance(**self._data[k])
