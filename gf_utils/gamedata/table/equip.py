from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class EquipInstance:
    id: int  # 1
    name: str  # 'BM 3-12X40'
    description: str  # '暴击概率+<critical_percent><%>\n$HG不可用'
    rank: int  # 2
    category: int  # 1
    type: int  # 1
    pow: str  # ''
    hit: str  # ''
    dodge: str  # ''
    speed: str  # ''
    rate: str  # ''
    critical_harm_rate: str  # ''
    critical_percent: str  # '5,8'
    armor_piercing: str  # ''
    armor: str  # ''
    shield: str  # ''
    damage_amplify: str  # ''
    damage_reduction: str  # ''
    night_view_percent: str  # ''
    bullet_number_up: str  # ''
    skill_effect_per: int  # 0
    skill_effect: int  # 0
    slow_down_percent: int  # 0
    slow_down_rate: int  # 0
    slow_down_time: int  # 0
    dot_percent: int  # 0
    dot_damage: int  # 0
    dot_time: int  # 0
    retire_mp: int  # 1
    retire_ammo: int  # 0
    retire_mre: int  # 1
    retire_part: int  # 0
    code: str  # '配件_光学瞄准镜_N'
    develop_duration: int  # 300
    company: str  # 'BM'
    skill_level_up: int  # 0
    fit_guns: str  # ''
    equip_introduction: str  # 'BM公司生产的3-12倍光学瞄准镜，让战术少女更容易命中敌人要害，除手枪外均可装配。'
    powerup_mp: float  # 0.0
    powerup_ammo: float  # 0.0
    powerup_mre: float  # 0.0
    powerup_part: float  # 0.0
    exclusive_rate: float  # 1.0
    bonus_type: str  # ''
    skill: int  # 0
    passive_skill: str  # '0'
    max_level: int  # 0
    auto_select_id: int  # 1001
    equip_group_id: int  # 0
    is_addition: int  # 0
    is_show: int  # 1
    obtain_ids: str  # '3,3001'
    sp_description: str  # 'equip-40000001'


class Equip(ConfigTable):
    name = "equip"

    def add_instance(self, k):
        return EquipInstance(**self._data[k])
