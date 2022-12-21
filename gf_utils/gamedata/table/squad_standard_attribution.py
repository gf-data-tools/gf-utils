
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class SquadStandardAttributionInstance:
    id:int # 1
    attribute_type:str # 'assist_damage'
    name:str # '*支援伤害'
    standard_attribute:float # 1.28
    cpu_standard_attribute:float # 4.4
    basic_rate:int # 40
    cpu_rate:int # 60
    role_id:int # 1

class SquadStandardAttribution(ConfigTable):
    name = 'squad_standard_attribution'

    def add_instance(self,k):
        return SquadStandardAttributionInstance(**self._data[k])    
