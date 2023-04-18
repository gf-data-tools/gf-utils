from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class MissionTargettrainEnemyInstance:
    id: int  # 101
    name: str  # '定制标靶'
    des: str  # '定制标靶'
    power: int  # 3000
    recommend_power: int  # 3000
    enemy_team_id: int  # 950046
    log_fitter_id: int  # 0
    log_fitter_name: str  # '定制标靶'
    code: str  # 'Targettrain_SingleTarget'
    fight_type: int  # 0
    type_coef: str  # ''
    fight_environment_group: str  # ''


class MissionTargettrainEnemy(ConfigTable):
    name = "mission_targettrain_enemy"

    def add_instance(self, k):
        return MissionTargettrainEnemyInstance(**self._data[k])
