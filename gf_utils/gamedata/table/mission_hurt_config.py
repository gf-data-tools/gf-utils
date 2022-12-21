
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class MissionHurtConfigInstance:
    id:int # 1
    name:str # '【标记】地雷爆炸伤害'
    target_type:int # 2
    type:int # 1
    is_number:int # 0
    life_type:int # 1
    value:str # '*0'
    hostage_value:int # 1
    is_armor:int # 0
    effect_birth:int # 3
    effect_process_star:int # 0
    effect_process_end:int # 0
    effect_process_duration:int # 0
    defender_value:str # '0'

class MissionHurtConfig(ConfigTable):
    name = 'mission_hurt_config'

    def add_instance(self,k):
        return MissionHurtConfigInstance(**self._data[k])    
