from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class EnemyCharacterTypeInstance:
    id: int  # 9999
    type: int  # 0
    name: str  # 'enemy_character_type-20009999'
    enemy_info: str  # ''
    code: str  # ''
    maxlife: int  # 0
    pow: int  # 0
    hit: int  # 0
    dodge: int  # 0
    range: int  # 0
    speed: int  # 0
    number: int  # 0
    angle: int  # 0
    armor_piercing: int  # 0
    armor: int  # 0
    shield: int  # 0
    rate: int  # 0
    boss_hp: int  # 0
    defense: int  # 0
    def_break: int  # 0
    debuff_resistance: float  # 0.0
    level: int  # 1
    character: str  # '投弹'
    special_attack: int  # 0
    normal_attack: int  # 300301
    passive_skill: str  # '200304'
    effect_ratio: float  # 1.0
    unable_buff_type: str  # ''
    able_buff_id: str  # ''
    voice: str  # ''
    deployment_scale: float  # 1.0
    recommend_description: str  # 'enemy_character_type-30009999'
    hit_point: str  # ''
    offset: str  # ''
    lifebar_offset: str  # ''
    enemy_illustration_id: int  # 0
    location_offset: str  # ''


class EnemyCharacterType(ConfigTable):
    name = "enemy_character_type"

    def add_instance(self, k):
        return EnemyCharacterTypeInstance(**self._data[k])
