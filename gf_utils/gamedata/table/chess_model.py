
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class ChessModelInstance:
    id:int # 1
    name:str # '标准'
    team_des:str # '个人混战'
    player_num:int # 4
    team_num:int # 1
    team_playerlimit:str # '4'
    prize:str # '10601,10602,10603,10604'

class ChessModel(ConfigTable):
    name = 'chess_model'

    def add_instance(self,k):
        return ChessModelInstance(**self._data[k])    
