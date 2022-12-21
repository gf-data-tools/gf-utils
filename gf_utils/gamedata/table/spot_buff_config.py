
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class SpotBuffConfigInstance:
    id:int # 1
    name:str # '出兵点'
    code:str # '1'
    type:int # 2
    vision_buff:str # '0'
    no_airborne:int # 0
    grow_enemy_pool:int # 1
    no_entry:int # 0

class SpotBuffConfig(ConfigTable):
    name = 'spot_buff_config'

    def add_instance(self,k):
        return SpotBuffConfigInstance(**self._data[k])    
