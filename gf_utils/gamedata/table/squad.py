from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class SquadInstance:
    id: int  # 1
    name: str  # 'BGM-71'
    en_name: str  # 'BGM-71'
    code: str  # 'TOW'
    introduce: str  # '喜爱桌游的四人小组，在战场上追求一击必胜，以便早些返回基地继续游戏。由于个性迥异，在团队做出决策时会以抽牌的方式排除不同意见。'
    dialogue: str  # 'squad-40000001'
    extra: str  # 'squad-50000001'
    en_introduce: str  # 'squad-60000001'
    type: int  # 1
    assist_type: int  # 1
    population: int  # 2
    cpu_id: int  # 1001
    hp: int  # 100
    assist_damage: int  # 125
    assist_reload: int  # 80
    assist_hit: int  # 135
    assist_def_break: int  # 140
    damage: int  # 100
    atk_speed: int  # 100
    hit: int  # 100
    basic_rate: int  # 110
    cpu_rate: int  # 90
    crit_rate: int  # 10
    crit_damage: int  # 150
    armor_piercing: int  # 0
    dodge: int  # 5
    move: int  # 5
    assist_armor_piercing: int  # 400
    battle_assist_range: str  # '1,2'
    display_assist_damage_area: int  # 150
    display_assist_area_coef: int  # 270
    attack_range: int  # 15
    night_vision: int  # 1
    skill1: int  # 500028
    skill2: int  # 500003
    skill3: int  # 500005
    performance_skill: int  # 900001
    passive_skill: str  # '500000,500029,500004,500024,501001'
    dynamic_passive_skill: str  # ''
    normal_attack: int  # 900107
    advanced_bonus: int  # 101
    deploy_round: int  # 0
    assist_attack_round: int  # 0
    attack_round: int  # 0
    baseammo: int  # 50
    basemre: int  # 50
    ammo_part: int  # 10
    mre_part: int  # 10
    is_additional: int  # 0
    launch_time: str  # '2016-05-20 00:00:00'
    obtain_ids: str  # '0'
    piece_item_id: int  # 301
    destroy_coef: int  # 100
    assist_damage_destroy_coef: int  # 0
    mission_skill_repair: str  # ''
    develop_duration: int  # 28800
    dorm_ai: str  # '1001,1002,1003'
    normal_attack_description: int  # 500000
    is_show: int  # 1
    org_id: int  # 10503


class Squad(ConfigTable):
    name = "squad"

    def add_instance(self, k):
        return SquadInstance(**self._data[k])
