from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class FairyInstance:
    id: int  # 1
    name: str  # '勇士妖精'
    code: str  # 'fighting'
    description: str  # '“什么都没结束！什么都没有，除了放假！”'
    introduce: str  # '拥有提高攻击效率的能力，平日可用于整理装备。'
    type: int  # 2
    pow: int  # 160
    hit: int  # 160
    dodge: int  # 100
    armor: int  # 100
    critical_harm_rate: int  # 0
    grow: int  # 100
    proportion: str  # '1:0.4,2:0.5,3:0.6,4:0.8,5:1'
    skill_id: str  # '900110'
    quality_exp: int  # 100
    quality_need_number: str  # '1:0,2:100,3:500,4:1500,5:3000'
    category: int  # 1
    develop_duration: int  # 16200
    retiremp: int  # 4
    retireammo: int  # 5
    retiremre: int  # 1
    retirepart: int  # 1
    powerup_mp: int  # 10
    powerup_ammo: int  # 14
    powerup_mre: int  # 3
    powerup_part: int  # 3
    armor_piercing: int  # 0
    ai: int  # 3000
    is_additional: int  # 0
    avatar_offset: str  # '-1.2,-1.2,0'
    avatar_scale: str  # '0.58,0.58,0.58'
    picture_offset: str  # '-60,-100,0'
    picture_scale: str  # '0.864,0.864,0.864'
    org_id: int  # 10502
    obtain_ids: str  # '39'
    skill_id_mod: str  # ''
    passive_skill_mod: str  # ''
    pow_mod: int  # 0
    hit_mod: int  # 0
    dodge_mod: int  # 0
    armor_mod: int  # 0
    critical_harm_rate_mod: int  # 0
    if_mod: int  # 0
    mod_exp: int  # 0


class Fairy(ConfigTable):
    name = "fairy"

    def add_instance(self, k):
        return FairyInstance(**self._data[k])
