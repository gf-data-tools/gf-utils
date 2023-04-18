from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class SummonerInstance:
    id: int  # 1
    name: str  # '1'
    code: str  # 'Drone'
    hp: int  # 400
    pow: int  # 1
    hit: int  # 1
    dodge: int  # 0
    range: int  # 1
    def_: int  # 9999
    def_percent: int  # 0
    def_break: int  # 0
    speed: int  # 5
    number: int  # 1
    angle: int  # 1
    armor_piercing: int  # 1
    armor: int  # 0
    crit_hit: int  # 0
    shield: int  # 1
    rate: int  # 1
    debuff_resistance: float  # 0.0
    level: int  # 1
    special_attack: int  # 0
    normal_attack: int  # 900107
    passive_skill: str  # '900105,900673'
    dynamic_passive_skill: str  # ''
    unable_buff_id: str  # '3250,3251,3252,3253,3254,3255'
    unable_buff_type: str  # ''
    scale: str  # '-0.9,0.9,0'
    start_offset: str  # '4,0,-2'
    camp: int  # 1
    is_stay: int  # 0
    is_hp_showed: int  # 1
    is_damage_showed: int  # 1
    is_damage_source: int  # 0
    is_sangvis: int  # 0
    phase_duration: int  # 0


class Summoner(ConfigTable):
    name = "summoner"

    def add_instance(self, k):
        return SummonerInstance(**self._data[k])
