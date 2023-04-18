from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class EnemyTeamInstance:
    id: int  # -2
    reward_gun_pool: str  # ''
    equip_s_probability: str  # ''
    draw_event_s_id: int  # 0
    enemy_leader: int  # 900013
    if_stay: int  # 0
    correction_belong: str  # ''
    correction_turn: str  # ''
    limit_guns: str  # ''
    limit_equips: str  # ''
    ai: int  # 0
    ai_content: str  # ''
    enemy_type_display: str  # ''
    use_building: str  # ''
    use_building_skill: str  # ''
    team_confrontfun_pic: str  # ''
    team_confrontfun_des: str  # 'enemy_team-9999998'
    effect_ext: int  # 0
    targettrain_cancollect: int  # 1
    fight_type: int  # 0
    type_coef: str  # ''


class EnemyTeam(ConfigTable):
    name = "enemy_team"

    def add_instance(self, k):
        return EnemyTeamInstance(**self._data[k])
