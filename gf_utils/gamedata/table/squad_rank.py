
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class SquadRankInstance:
    star_id:int # 1
    lv_unlock:str # '1'
    cost_self_piece:int # 5
    cpu_rate:int # 50

class SquadRank(ConfigTable):
    name = 'squad_rank'

    def add_instance(self,k):
        return SquadRankInstance(**self._data[k])    
