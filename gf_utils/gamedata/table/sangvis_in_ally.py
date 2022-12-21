
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class SangvisInAllyInstance:
    id:int # 1
    sangvis_id:int # 1001
    sangvis_level:int # 90
    life:int # 100
    sangvis_advance:int # 4
    sangvis_shape_n:int # 1
    sangvis_resolution_level:int # 3
    skill1:int # 8
    skill2:int # 1
    skill3:int # 5
    skill_advance:int # 0
    chip1:int # 1003
    chip2:int # 1001
    favor:int # 90000

class SangvisInAlly(ConfigTable):
    name = 'sangvis_in_ally'

    def add_instance(self,k):
        return SangvisInAllyInstance(**self._data[k])    
