
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class ExploreMallInstance:
    id:int # 1
    type:int # 1
    prize_id:int # 12101
    cost:str # '4001-15000'
    quota:int # 0
    clear_cycle:int # 0
    function_control_id:int # 0
    start_time:str # ''
    end_time:str # ''
    is_new:int # 0

class ExploreMall(ConfigTable):
    name = 'explore_mall'

    def add_instance(self,k):
        return ExploreMallInstance(**self._data[k])    
