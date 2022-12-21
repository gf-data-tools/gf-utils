
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class SangvisResolutionInstance:
    id:int # 10000
    group_id:int # 100
    lv:int # 0
    unlock_num:int # 0
    if_skill_up:int # 0
    resolution_number:int # 1
    resolution_hp:int # 366
    resolution_pow:int # 44
    resolution_rate:int # 38
    resolution_hit:int # 23
    resolution_dodge:int # 48
    resolution_armor:int # 0
    resolution_armor_piercing:int # 0
    resolution_crit:int # 0
    resolution_crit_dmg:int # 0
    resolution_speed:int # 0
    resolution_effect:int # 0
    effect_grid_effect:str # '4:2,6;4,9'
    ap_add:int # 0
    cost_reduce:int # 0
    skill1:int # 0
    skill2:int # 0
    skill3:int # 0
    skill_advance:int # 0

class SangvisResolution(ConfigTable):
    name = 'sangvis_resolution'

    def add_instance(self,k):
        return SangvisResolutionInstance(**self._data[k])    
