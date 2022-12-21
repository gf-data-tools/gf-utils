
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class DormActionInstance:
    id:int # 1
    spine_name:str # 'wait'
    interact_type:int # 0
    interact_point_type:str # '0'
    emoji:str # ''
    min_decorate:int # 0
    max_decorate:int # 0
    min_favor:int # 0
    max_favor:int # 0
    action_voice:str # ''
    action_sound:str # ''
    action_bgm:str # ''
    shadow_exist:int # 1
    move_speed:float # 0.0
    next_action:str # ''
    no_vertical_motion:int # 0
    is_married:int # 0
    furiniture_action_interact:str # ''
    default_action:str # ''

class DormAction(ConfigTable):
    name = 'dorm_action'

    def add_instance(self,k):
        return DormActionInstance(**self._data[k])    
