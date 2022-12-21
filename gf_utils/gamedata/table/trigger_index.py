
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class TriggerIndexInstance:
    id:int # 1
    type:int # 1
    special_spot_condition:str # ''
    mission_buff_condition:str # ''
    person_condition:str # ''

class TriggerIndex(ConfigTable):
    name = 'trigger_index'

    def add_instance(self,k):
        return TriggerIndexInstance(**self._data[k])    
