
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class TheaterConstructionInstance:
    id:int # 41100
    name:str # '前进基地'
    group_id:int # 411
    lv:int # 0
    description:str # '远征队梯队数量+0'
    code:str # 'TheaterConstruction0'
    material_rate:int # 3
    construction_pt:int # 0
    effect:str # '41100'
    area_id:int # 411
    material_item:int # 47
    material_number:int # 10

class TheaterConstruction(ConfigTable):
    name = 'theater_construction'

    def add_instance(self,k):
        return TheaterConstructionInstance(**self._data[k])    
