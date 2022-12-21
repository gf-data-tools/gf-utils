
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class ChessSeasoneventInstance:
    id:int # 1
    name:str # '拉弗伯雷.Beta1'
    start_time:str # '2021-07-16 10:04:00'
    end_time:str # '2021-07-31 10:04:00'
    mission_id:int # 1

class ChessSeasonevent(ConfigTable):
    name = 'chess_seasonevent'

    def add_instance(self,k):
        return ChessSeasoneventInstance(**self._data[k])    
