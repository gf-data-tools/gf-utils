from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class TheaterAreaInstance:
    id: int  # 411
    name: str  # '普通关卡'
    fight_type: int  # 1
    type_coef: str  # '0'
    success_type_condition: str  # '1;3;6'
    basic_score: int  # 300
    fight_environment_group: str  # '1;3;6'
    is_enemy_random: int  # 0
    theater_spare_gun_num: int  # 10
    theater_spare_fairy_num: int  # 0
    theater_spare_sangvis_cost: int  # 10
    assist_npc: str  # ''
    assist_squad: str  # ''
    assist_fairy: str  # ''
    boss_score_coef: str  # '100;0;50;0;200;50;100;00;100;50;00;100;100'
    boss_score_display: str  # '-2;0;0;0;2;0;1;0;1;0;0;-1;0'
    start_score: int  # 0
    end_score: int  # 12000000
    type: int  # 1
    construction: str  # '411'
    enemy_group: str  # '1843-0-4,1846-0-4,1847-0-4'
    enemy_lv: str  # '-30,-29,-28,-27,-26,-25,-24,-23,-22,-21'
    enemy_score: str  # '70,71,72,73,74,75,76,77,78,80'
    occupied_enemy_lv: str  # '-34,-34,-33,-32,-32,-31,-31,-30,-29,-28'
    occupied_enemy_score: str  # '70,71,72,73,74,75,76,77,78,80'
    boss: str  # ''
    occupied_boss_score: int  # 60
    score_limit: int  # 0
    advantage_gun: str  # '36,26,100'
    material_item: int  # 47
    battle_background: str  # 'wasteland'
    theater_id: int  # 41
    display_length: int  # 300
    description: str  # '被枪林弹雨洗礼的山头，是我们前进的第一道障碍。为了下一阶段的作战，我们要拿下这片区域，作为前进的立足点。'
    difficulty: int  # 1000
    area_mission_id: int  # 900411
    advantage_sangvis: str  # ''
    advantage_skill: str  # ''
    advantage_desc: str  # '这是优势人形技能描述'


class TheaterArea(ConfigTable):
    name = "theater_area"

    def add_instance(self, k):
        return TheaterAreaInstance(**self._data[k])
