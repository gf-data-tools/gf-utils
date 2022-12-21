
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class SquadTypeInstance:
    type_id:int # 1
    name:str # '反坦克武器'
    en_name:str # 'Anti-Tank Weapon'
    class_name:str # '火力单位'
    class_en_name:str # 'Fire Support Unit'
    hp:float # 1.0
    assist_damage:float # 147.51
    assist_reload:float # 53.53
    assist_hit:float # 126.96
    assist_def_break:float # 157.82
    damage:float # 0.0
    atk_speed:float # 0.0
    hit:float # 0.0
    def:float # 0.0
    fix_type:int # 1
    fix_time:float # 60.0
    mp_fix:float # 1.0
    part_fix:float # 0.5

class SquadType(ConfigTable):
    name = 'squad_type'

    def add_instance(self,k):
        return SquadTypeInstance(**self._data[k])    
