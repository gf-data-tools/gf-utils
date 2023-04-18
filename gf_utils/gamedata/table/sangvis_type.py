from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class SangvisTypeInstance:
    id: int  # 1
    name: str  # 'BOSS'
    basic_hp: float  # 4.79
    basic_pow: float  # 3.67
    basic_rate: float  # 0.46
    basic_speed: float  # 1.0
    basic_hit: float  # 0.55
    basic_dodge: float  # 0.75
    basic_armor: float  # 0.18
    mp_fix_ratio: float  # 9.0
    part_fix_ratio: float  # 3.0
    fix_time_ratio: float  # 2.0
    skill_advance_lv: int  # 4
    pic_advance_lv: int  # 5
    daily_successr: int  # 2500
    author_successr: int  # 10000
    default_advance_lv: int  # 3
    exchange_num: str  # '512:100'
    repair_cost: int  # 1
    trans_num: str  # '-1,-1'
    skills_max_lv: str  # '10,10,5,5'


class SangvisType(ConfigTable):
    name = "sangvis_type"

    def add_instance(self, k):
        return SangvisTypeInstance(**self._data[k])
