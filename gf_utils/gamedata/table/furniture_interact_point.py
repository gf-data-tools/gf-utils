
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class FurnitureInteractPointInstance:
    id:int # 1
    gun_action:str # 'sit'
    is_cover:int # 0
    sorting:int # 0
    furiniture_action_interact:str # ''
    direction:int # -1
    bone_name:str # ''
    initial_angle:int # 0
    end_action:str # 'sit'
    need_action:str # ''
    group:str # ''

class FurnitureInteractPoint(ConfigTable):
    name = 'furniture_interact_point'

    def add_instance(self,k):
        return FurnitureInteractPointInstance(**self._data[k])    
