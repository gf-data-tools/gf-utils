
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class ExploreItemInstance:
    id:int # 6001
    explore_time_down:float # 0.9
    mid_reward_up:float # 1.0
    reward1_up:float # 1.0
    area_id_up:str # ''

class ExploreItem(ConfigTable):
    name = 'explore_item'

    def add_instance(self,k):
        return ExploreItemInstance(**self._data[k])    
